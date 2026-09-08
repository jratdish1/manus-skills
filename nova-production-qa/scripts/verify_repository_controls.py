#!/usr/bin/env python3
"""Verify non-secret controls for the public Nova skills repository.

This program is read-only except for an explicitly requested JSON result file. It
never reads environment variables, uses network services, runs user-provided
commands, publishes content, changes schedules, uploads files, or deletes data.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


REQUIRED_FILES = (
    "README.md",
    "nova-bible-audit/SKILL.md",
    "brag-nova/SKILL.md",
    "nova-shorts-package/SKILL.md",
    "nova-caption-pack/SKILL.md",
    "nova-production-qa/SKILL.md",
    "nova-production-qa/references/VETS_STANDING_AUDIT_DIRECTIVE.md",
    "nova-production-qa/references/GROK_BOT_AUDIT_HANDOFF.md",
    "nova-production-qa/references/EXACT_REFERENCE_BINDING.md",
    "nova-production-qa/references/PRODUCTION_AUTHORIZATION_AND_EVIDENCE.md",
    "nova-production-qa/references/VERIFICATION_OPERATIONS.md",
    "nova-production-qa/scripts/verify_production_gate.py",
    "nova-production-qa/scripts/verify_repository_controls.py",
    ".github/workflows/nova-production-qa-controls.yml",
)

SECRET_PATTERNS = (
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bxai-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAIza[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b"),
)


def check(name: str, passed: bool, detail: str) -> dict[str, Any]:
    """Create a normalized check result."""
    return {"name": name, "status": "PASS" if passed else "FAIL", "detail": detail}


def tracked_files(repo: Path) -> list[Path]:
    """Return Git-tracked and untracked non-ignored regular files under repo."""
    command = ["git", "-C", str(repo), "ls-files", "-co", "--exclude-standard"]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    files: list[Path] = []
    for relative in result.stdout.splitlines():
        candidate = repo / relative
        if candidate.is_file():
            files.append(candidate)
    return files


def git_diff_check(repo: Path) -> tuple[bool, str]:
    """Run a bounded Git whitespace check against the latest parent when available."""
    parent = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--verify", "HEAD^"],
        capture_output=True,
        text=True,
    )
    command = ["git", "-C", str(repo), "diff", "--check"]
    if parent.returncode == 0:
        command.extend(["HEAD^", "HEAD"])
    result = subprocess.run(command, capture_output=True, text=True)
    detail = (result.stdout + result.stderr).strip() or "No whitespace errors detected"
    return result.returncode == 0, detail


def frontmatter_check(repo: Path) -> list[dict[str, Any]]:
    """Validate basic SKILL.md metadata and the 500-line skill limit."""
    results: list[dict[str, Any]] = []
    for skill in sorted(repo.glob("*/SKILL.md")):
        lines = skill.read_text(encoding="utf-8").splitlines()
        expected_name = skill.parent.name
        is_valid = (
            len(lines) < 500
            and len(lines) >= 4
            and lines[0] == "---"
            and lines[1] == f"name: {expected_name}"
            and lines[2].startswith("description: ")
            and lines[3] == "---"
        )
        results.append(
            check(
                f"frontmatter:{skill.relative_to(repo)}",
                is_valid,
                f"{len(lines)} lines; expected name={expected_name}",
            )
        )
    return results


def secret_scan(repo: Path) -> tuple[bool, str]:
    """Scan repository files for high-confidence secret-token formats."""
    matches: list[str] = []
    for file_path in tracked_files(repo):
        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(content.splitlines(), start=1):
            if any(pattern.search(line) for pattern in SECRET_PATTERNS):
                matches.append(f"{file_path.relative_to(repo)}:{line_number}")
    if matches:
        return False, "Potential credential pattern(s): " + ", ".join(matches)
    return True, "No high-confidence credential patterns found"


def compile_scripts(repo: Path) -> tuple[bool, str]:
    """Compile bundled Python files in memory without creating bytecode files."""
    failures: list[str] = []
    for script in sorted(repo.glob("**/*.py")):
        try:
            compile(script.read_text(encoding="utf-8"), str(script), "exec")
        except (OSError, UnicodeDecodeError, SyntaxError) as error:
            failures.append(f"{script.relative_to(repo)}: {error}")
    if failures:
        return False, "; ".join(failures)
    return True, "All bundled Python scripts compile in memory"


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Nova skills repository-control verifier")
    parser.add_argument("--repo", required=True, type=Path, help="Local Git checkout to verify")
    parser.add_argument("--result", type=Path, help="Optional non-secret JSON result output")
    arguments = parser.parse_args()

    repo = arguments.repo.resolve()
    checks: list[dict[str, Any]] = []
    if not (repo / ".git").exists():
        checks.append(check("git-checkout", False, "--repo must be a local Git checkout"))
    else:
        missing = [path for path in REQUIRED_FILES if not (repo / path).is_file()]
        checks.append(check("required-files", not missing, "All required files present" if not missing else "Missing: " + ", ".join(missing)))
        checks.extend(frontmatter_check(repo))
        whitespace_ok, whitespace_detail = git_diff_check(repo)
        checks.append(check("git-diff-check", whitespace_ok, whitespace_detail))
        secret_ok, secret_detail = secret_scan(repo)
        checks.append(check("credential-pattern-scan", secret_ok, secret_detail))
        compile_ok, compile_detail = compile_scripts(repo)
        checks.append(check("python-compilation", compile_ok, compile_detail))
        readme = (repo / "README.md").read_text(encoding="utf-8") if (repo / "README.md").is_file() else ""
        references = (
            "VETS Standing Audit Directive",
            "Grok-Bot Audit Handoff",
            "Exact Reference Binding",
            "Production Authorization and Evidence",
        )
        links_ok = all(reference in readme for reference in references)
        checks.append(check("public-index", links_ok, "Required audit and handoff references present in README" if links_ok else "README lacks one or more required audit references"))

    errors = [item["detail"] for item in checks if item["status"] == "FAIL"]
    result = {"overall_status": "PASS" if not errors else "FAIL", "checks": checks, "errors": errors}
    output = json.dumps(result, indent=2) + "\n"
    if arguments.result:
        arguments.result.parent.mkdir(parents=True, exist_ok=True)
        arguments.result.write_text(output, encoding="utf-8")
    sys.stdout.write(output)
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
