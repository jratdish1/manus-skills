# Verification Operations

Run the following checks on **every pull request and every push** that changes the public `jratdish1/manus-skills` repository. Run the production authorization verifier again immediately before any live scheduling, publication, or production configuration mutation.

## Governance Responsibility and Cadence

| Responsible party | Required action | Trigger |
|---|---|---|
| Implementation agent | Run the repository-control verifier locally before requesting review or creating a release candidate; preserve the non-secret result. | Every source revision. |
| GitHub Actions | Run the same repository-control verifier and retain the result artifact. | Every pull request and every push. |
| Independent OpenAI/ChatGPT auditor | Review the exact source and artifact evidence under the VETS rubric. | After the final revision/artifact is assembled and after any material change. |
| VETS | Review the complete evidence package and provide the checksum-bound authorization record for any live production action. | Immediately before any publication, schedule, or production configuration mutation. |
| VETS or delegated named operator | Reconfirm the control set, retention, access, and branch-protection posture. | Quarterly and after any incident, unauthorized-mutation attempt, or repository-access change. |

A failed check, expired approval, source/artifact checksum mismatch, or absent evidence requires immediate `HOLD`. Do not defer the failure to the next scheduled review.

## Required Checks

| Control | When | Command | Pass condition | Failure handling |
|---|---|---|---|---|
| Repository-control scan | Every pull request and push | `python3 nova-production-qa/scripts/verify_repository_controls.py --repo . --result /tmp/nova-repository-controls.json` | Exit code `0`; JSON `overall_status` is `PASS`. | Do not merge or treat the revision as audit-ready. Fix the stated error(s), rerun the scan, then obtain a new exact-SHA audit. |
| Exact approval gate | Immediately before a live action | `python3 nova-production-qa/scripts/verify_production_gate.py --approval <non-secret-approval.json> --final-video <final.mp4> --final-audio <final.mp3> --expected-head-sha <SHA> --result <result.json>` | Exit code `0`; JSON `overall_status` is `GO`. | Do not publish, schedule, upload, or change production. Correct the mismatch or missing approval, then rerun. |
| Independent OpenAI/ChatGPT audit | After final source/artifact checks and before a Grade-A claim | Use an official OpenAI/ChatGPT audit path with the exact final SHA and artifact checksums. | Complete non-secret audit evidence supports the VETS rubric. | If head/artifact changes, return `AUDIT STALE — HEAD CHANGED`; if findings remain, remediate or receive explicit VETS disposition before rerun. |

## Machine-Readable Results

Both scripts emit JSON to standard output and optionally to `--result`. Treat the exit code and `overall_status` as authoritative:

| Exit code | Meaning | Required result |
|---:|---|---|
| `0` | The verification passed. | Repository: `PASS`; authorization gate: `GO`. |
| `2` | A required control failed or required evidence is missing/mismatched. | Repository: `FAIL`; authorization: `HOLD`. |
| Other non-zero | Execution failure or invalid invocation. | `AUDIT INCOMPLETE`; do not infer a pass. |

Record both the result file checksum and the exact final source SHA in the private evidence folder.

## Required Scans

The repository-control scan performs these fixed, non-networked checks:

1. Required skills and audit-reference files exist and are non-empty.
2. `SKILL.md` YAML front matter contains the correct skill name and description; the file remains under the 500-line skill limit.
3. Markdown has no whitespace errors detectable by `git diff --check`.
4. Tracked files contain no recognized high-confidence secret-token patterns.
5. Bundled Python scripts compile in memory without creating bytecode files.
6. Public documentation includes the audit, authorization, source-binding, and Grok-bot handoff references.

The scan never reads environment variables, makes network calls, publishes content, changes schedules, deletes files, or executes user-supplied shell commands.

## Audit-Ready Decision

Return the following only after the exact final HEAD and final artifact checksums remain unchanged since the preserved independent audit:

```text
AUDIT STATUS: PASS — GRADE A
```

Otherwise return the relevant `AUDIT REQUIRED`, `AUDIT STALE — HEAD CHANGED`, `AUDIT INCOMPLETE`, `FINDINGS REMAIN`, `HUMAN_REVIEW_REQUIRED`, or `SOURCE_UNAVAILABLE` status.

## GitHub Enforcement

The repository includes a GitHub Actions workflow that runs the repository-control scan for every pull request and push. Configure repository branch protection or rulesets so **Nova Production QA Controls / verify** is required before merging a pull request into `main`. Do not rely on a green check from an earlier SHA.

## Evidence Format and Size Limits

Keep evidence structured and bounded. Approval records and verifier results must be UTF-8 JSON no larger than **1 MiB**. Independent audit evidence must be UTF-8 JSON or Markdown no larger than **10 MiB** per file. For larger outputs, split files into ordered, individually checksummed parts and record a manifest. Store video, audio, image, and archive artifacts separately; preserve their filename, size, MIME/type, and SHA-256 in the evidence record rather than embedding binary data in a Markdown or JSON audit log.

Reject malformed, unparseable, oversized, or unchecksummed evidence as `AUDIT INCOMPLETE`. Never use an oversized evidence file as a reason to omit a required audit; split it safely and retain all parts.

## Retention and Privacy

Keep complete non-secret audit outputs, the approval record, test results, SHA-256 checksums, and rollback record in the private source-of-truth repository for at least 24 months. Keep public reports sanitized. The repository-control scan executes on every pull request and every push; a named VETS/delegated-operator review occurs at least quarterly. Never place credentials, tokens, private URLs, cookies, secrets, or protected user data in the public skills repository or publicly visible Actions logs.
