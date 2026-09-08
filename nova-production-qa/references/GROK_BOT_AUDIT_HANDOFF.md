# Grok-Bot Audit Handoff

Use this document with the public `nova-production-qa` skill and the `VETS_STANDING_AUDIT_DIRECTIVE.md` reference when Grok-bot is asked to perform **advisory** evaluation of a Nova Reign asset or production package.

## Authority and Boundaries

Grok-bot may independently inspect final artifacts, identify deficiencies, compare them against the Nova Bible and this QA skill, and provide an adversarial findings report. Grok-bot must not audit and certify its own implementation. It must not publish, schedule, modify production systems, or handle secrets.

A Grok-bot response is advisory evidence unless it is an authenticated, attributable, reproducible official audit run that is tied to the exact final artifact. VETS retains final approval authority.

## Required Handoff Package

Provide all of the following, with no secrets:

| Item | What to provide |
|---|---|
| Skill source | Exact GitHub commit URL for `nova-production-qa/SKILL.md`. |
| Audit directive | Exact GitHub commit URL for `references/VETS_STANDING_AUDIT_DIRECTIVE.md`. |
| Final artifact | Final MP4/image/audio file or controlled public review URL. |
| Artifact binding | SHA-256 checksum, filename, file size, duration, resolution, codec, and creation timestamp. |
| Source binding | Repository, branch, base SHA, final head SHA, and changed-file list where source-controlled content is involved. |
| Nova audit input | Exact Grok image prompt, negative prompt, Nova Bible audit result, and representative opening/middle/end frames. |
| Production evidence | Audio QA, video QA, test results, security scans, failures, fixes, and rollback procedure. |
| Scene context | Episode number, assigned scene/activity, and relevant Scene Diversity Bible entry. |

## Paste This to Grok

```text
You are an independent adversarial reviewer. Do not restate the implementation claims. Review the supplied exact final artifact and evidence package against the linked Nova Production QA skill and VETS Standing Audit Directive.

Your task is advisory only. You may not publish, schedule, mutate systems, request or expose secrets, or certify your own implementation.

Verify:
1. Exact-artifact binding: repository, branch, base SHA, final SHA, changed files, and artifact checksum.
2. Nova Bible compliance: character appearance, dog tags, 9:16 composition, SFW standard, and tattoo orientation. LEFT side of the frame must be Nova's right arm with the eagle sleeve, 1776, and E Pluribus Unum. RIGHT side must be bare with zero tattoos.
3. Visual quality: natural human motion, proportional body/head relationship, emotion, no robotic or repetitive movement, unique background/activity.
4. Audio quality: natural delivery, no startup echo, feedback, pop, clipping, duplicated layer, or synchronization issue.
5. Production controls: explicit VETS approval state, no unauthorized publishing, tests/scans, rollback, and non-secret evidence preservation.

Return exactly:
- Audit tool native grade: NONE unless your authenticated official tool produces a grade.
- Findings grouped by Critical / High / Medium / Low, with evidence references.
- Required remediation and retest scope.
- Whether the evidence supports VETS rubric grade A, B, C, or HOLD. State that this is a rubric recommendation rather than a native tool grade if applicable.
- Head changed after audit: YES / NO / UNKNOWN.
- Final advisory status: AUDIT STATUS: PASS — GRADE A / AUDIT REQUIRED / AUDIT STALE — HEAD CHANGED / AUDIT INCOMPLETE / FINDINGS REMAIN / HUMAN_REVIEW_REQUIRED / SOURCE_UNAVAILABLE.

Do not invent outputs, tool versions, test results, timestamps, SHAs, checksums, grades, or artifact details.
```

## Evidence Storage Standard

Store the complete non-secret prompt, full response, run/session ID when present, artifact checksum, timestamps in Pacific and UTC, source SHA, findings, remediation rounds, test results, and scan results in a durable evidence path. Keep only sanitized summaries in public status reports.

## Final Approval Rule

An advisory finding of no issues does not authorize publishing. Require the final `nova-production-qa` decision and explicit VETS GO before a live post.
