#!/usr/bin/env python3
"""Verify a checksum-bound VETS approval record without mutating production.

This program is intentionally read-only. It never publishes, schedules, uploads,
deletes, calls a network service, or reads environment variables. It verifies
whether a supplied non-secret approval record is internally complete and bound
to the final video/audio file checksums and expected source SHA.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ALLOWED_ACTIONS = {"publish", "schedule", "production-config-change", "approval-only"}
REQUIRED_BINDING_FIELDS = {"repository", "branch", "commit_sha", "file_path", "file_sha256"}


def sha256(path: Path) -> str:
    """Return the SHA-256 digest for a file in bounded chunks."""
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_timestamp(value: str) -> bool:
    """Return true only for parseable ISO-8601 timestamps with UTC offset."""
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return False
    return parsed.tzinfo is not None


def is_sha256(value: Any) -> bool:
    """Return true only for a lowercase or uppercase 64-character hex digest."""
    if not isinstance(value, str) or len(value) != 64:
        return False
    return all(character in "0123456789abcdefABCDEF" for character in value)


def add_error(errors: list[str], condition: bool, message: str) -> None:
    """Append a validation message if a required condition is false."""
    if not condition:
        errors.append(message)


def load_record(path: Path) -> dict[str, Any]:
    """Load a JSON approval record and reject files larger than one MiB."""
    if not path.is_file():
        raise ValueError(f"Approval record does not exist: {path}")
    if path.stat().st_size > 1024 * 1024:
        raise ValueError("Approval record exceeds the one MiB safety limit")
    try:
        content = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"Approval record is not valid UTF-8 JSON: {error}") from error
    if not isinstance(content, dict):
        raise ValueError("Approval record root must be a JSON object")
    return content


def validate_record(
    record: dict[str, Any],
    final_video: Path | None,
    final_audio: Path | None,
    expected_head_sha: str | None,
) -> list[str]:
    """Validate source, evidence, VETS approval, and provided artifact bindings."""
    errors: list[str] = []
    action = record.get("requested_action")
    add_error(errors, isinstance(record.get("package_id"), str) and bool(record["package_id"].strip()), "package_id is required")
    add_error(errors, isinstance(record.get("episode"), str) and bool(record["episode"].strip()), "episode is required")
    add_error(errors, action in ALLOWED_ACTIONS, "requested_action must be publish, schedule, production-config-change, or approval-only")

    source = record.get("source")
    add_error(errors, isinstance(source, dict), "source object is required")
    if isinstance(source, dict):
        for key in ("repository", "branch", "base_sha", "final_head_sha", "changed_files"):
            add_error(errors, bool(source.get(key)), f"source.{key} is required")
        add_error(errors, isinstance(source.get("changed_files"), list), "source.changed_files must be a list")
        if expected_head_sha:
            add_error(errors, source.get("final_head_sha") == expected_head_sha, "source.final_head_sha does not match --expected-head-sha")

    bindings = record.get("source_reference_bindings")
    add_error(errors, isinstance(bindings, list) and bool(bindings), "source_reference_bindings must contain at least one immutable binding")
    if isinstance(bindings, list):
        for index, binding in enumerate(bindings):
            add_error(errors, isinstance(binding, dict), f"binding {index} must be an object")
            if isinstance(binding, dict):
                missing = REQUIRED_BINDING_FIELDS - set(binding)
                add_error(errors, not missing, f"binding {index} lacks: {', '.join(sorted(missing))}")
                add_error(errors, is_sha256(binding.get("file_sha256")), f"binding {index}.file_sha256 is invalid")

    audit = record.get("openai_audit")
    add_error(errors, isinstance(audit, dict), "openai_audit object is required")
    if isinstance(audit, dict):
        add_error(errors, audit.get("status") == "AUDIT STATUS: PASS — GRADE A", "openai_audit.status must be exact Grade-A PASS")
        add_error(errors, audit.get("native_tool_grade") == "NONE", "openai_audit.native_tool_grade must be NONE when no native grade exists")
        add_error(errors, audit.get("vets_rubric_grade") == "A", "openai_audit.vets_rubric_grade must be A")
        add_error(errors, isinstance(audit.get("evidence_path"), str) and bool(audit["evidence_path"]), "openai_audit.evidence_path is required")
        add_error(errors, is_sha256(audit.get("evidence_sha256")), "openai_audit.evidence_sha256 is invalid")

    add_error(errors, record.get("qa_result") == "PASS", "qa_result must be PASS")
    add_error(errors, isinstance(record.get("rollback_plan"), str) and bool(record["rollback_plan"].strip()), "rollback_plan is required")

    approval = record.get("operator_approval")
    add_error(errors, isinstance(approval, dict), "operator_approval object is required")
    if isinstance(approval, dict):
        add_error(errors, approval.get("approved_by") == "VETS", "operator_approval.approved_by must equal VETS")
        add_error(errors, isinstance(approval.get("approval_reference"), str) and bool(approval["approval_reference"].strip()), "operator_approval.approval_reference is required")
        add_error(errors, approval.get("approved_action") == action, "operator_approval.approved_action must match requested_action")
        add_error(errors, parse_timestamp(approval.get("approval_timestamp_pacific")), "operator_approval.approval_timestamp_pacific must be ISO-8601 with offset")
        add_error(errors, parse_timestamp(approval.get("approval_timestamp_utc")), "operator_approval.approval_timestamp_utc must be ISO-8601 with offset")

    artifacts = record.get("artifacts")
    add_error(errors, isinstance(artifacts, dict), "artifacts object is required")
    video = artifacts.get("video") if isinstance(artifacts, dict) else None
    audio = artifacts.get("audio") if isinstance(artifacts, dict) else None

    requires_video = action in {"publish", "schedule"}
    if requires_video:
        add_error(errors, isinstance(video, dict), "artifacts.video is required for publish or schedule")
        add_error(errors, final_video is not None and final_video.is_file(), "--final-video is required and must exist for publish or schedule")
    if isinstance(video, dict) and final_video and final_video.is_file():
        expected = video.get("sha256")
        actual = sha256(final_video)
        add_error(errors, is_sha256(expected), "artifacts.video.sha256 is invalid")
        add_error(errors, expected == actual, "final video SHA-256 does not match artifacts.video.sha256")
        if isinstance(approval, dict):
            add_error(errors, approval.get("approved_artifact_sha256") == actual, "operator approval is not bound to the final video SHA-256")

    if final_audio is not None:
        add_error(errors, final_audio.is_file(), "--final-audio must exist when supplied")
    if isinstance(audio, dict) and final_audio and final_audio.is_file():
        expected = audio.get("sha256")
        actual = sha256(final_audio)
        add_error(errors, is_sha256(expected), "artifacts.audio.sha256 is invalid")
        add_error(errors, expected == actual, "final audio SHA-256 does not match artifacts.audio.sha256")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only VETS production authorization gate verifier")
    parser.add_argument("--approval", required=True, type=Path, help="Path to non-secret JSON approval record")
    parser.add_argument("--final-video", type=Path, help="Path to final video for checksum verification")
    parser.add_argument("--final-audio", type=Path, help="Path to final audio for checksum verification")
    parser.add_argument("--expected-head-sha", help="Expected exact final source SHA")
    parser.add_argument("--result", type=Path, help="Optional non-secret JSON result path")
    arguments = parser.parse_args()

    try:
        record = load_record(arguments.approval)
        errors = validate_record(record, arguments.final_video, arguments.final_audio, arguments.expected_head_sha)
    except ValueError as error:
        errors = [str(error)]

    result = {
        "overall_status": "GO" if not errors else "HOLD",
        "production_authorization": "PASS" if not errors else "HUMAN_REVIEW_REQUIRED",
        "approval_record": str(arguments.approval),
        "final_video": str(arguments.final_video) if arguments.final_video else None,
        "final_audio": str(arguments.final_audio) if arguments.final_audio else None,
        "errors": errors,
    }
    output = json.dumps(result, indent=2) + "\n"
    if arguments.result:
        arguments.result.parent.mkdir(parents=True, exist_ok=True)
        arguments.result.write_text(output, encoding="utf-8")
    sys.stdout.write(output)
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
