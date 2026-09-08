---
name: nova-production-qa
description: Perform final quality assurance on Nova Reign Boot Camp Chaos video packages before any publication. Use to enforce the motion-first pipeline, scene diversity, Nova Bible checks, VETS Standing Audit Directive, evidence preservation, and production GO/NO-GO decisions.
---

# Nova Production QA

Perform the final quality-assurance gate for a complete Nova video package. Do **not** publish, schedule, or mutate production platforms without explicit VETS authorization.

## Required Inputs

Collect the final rendered video, final audio, final metadata/captions, source revision (when applicable), prior episode scene registry, and relevant audit evidence. If any final artifact is absent, return `AUDIT INCOMPLETE` and identify the missing item.

## V2 Production Rules — Mandatory

1. Use a **motion-first** source: create a moving base clip with natural breathing, weight shifts, expression, and body-language cues. Reject static-photo-avatar output or body/head compositing that reads as robotic.
2. Prepare clean audio before ingest: trim startup artifact, apply a short fade-in, normalize safely, and verify no startup pop, echo, feedback, clipping, or accidental double-track remains.
3. Require natural lip-sync when lip-sync is part of the final video. If the selected workflow cannot achieve it, report the limitation and hold the final delivery for VETS review.
4. Enforce **scene diversity**. Do not reuse an earlier episode’s background, activity, or primary environment. Consult the Scene Diversity Bible and reject duplicates.
5. Maintain SFW, veteran- and first-responder-friendly content. Do not publish on the basis of a dry-run package alone.

## Visual QA

Refer to `nova-bible-audit` for the full character audit. Verify all of the following on representative opening, mid-point, and ending frames:

- [ ] 9:16 vertical delivery format.
- [ ] Hazel amber/golden-brown eyes, athletic build, warm medium-brown skin, long dark wavy/curly hair, and visible dog tags.
- [ ] **LEFT side of the image/frame** is Nova’s right arm and visibly carries the full American flag bald eagle sleeve with `1776` and `E Pluribus Unum`.
- [ ] **RIGHT side of the image/frame** is Nova’s left arm and remains bare with zero tattoos or markings.
- [ ] Motion is human and proportional: natural breathing, posture, gestures, and emotion; no frozen torso, head-on-body illusion, or robotic repetition.
- [ ] Background and activity are unique for the episode and match the approved scene plan.
- [ ] No explicit, graphic, deceptive, or unsafe content.

If tattoo orientation is wrong, return `REJECT` immediately.

## Audio QA

- [ ] Voice delivery matches Nova’s witty, sarcastic, resilient mockumentary tone.
- [ ] Spoken script, pacing, and pauses are clear and natural.
- [ ] No startup feedback, echo, pop, clipping, phase artifacts, or duplicated voice layer.
- [ ] Audio/video duration and synchronization are correct.

## Metadata QA

- [ ] Title is concise, curiosity-driven, and platform-safe.
- [ ] Description includes a relevant CTA or question.
- [ ] Captions are adapted for YouTube Shorts, Instagram Reels, TikTok, Fanvue, and X as applicable.
- [ ] Platform-specific claims, hashtags, and terminology are accurate and SFW.
- [ ] Publishing remains on hold until explicit VETS GO.

# VETS Standing Audit Directive — Required Gate

Read [`references/VETS_STANDING_AUDIT_DIRECTIVE.md`](references/VETS_STANDING_AUDIT_DIRECTIVE.md) before making an audit-grade claim or approving any code, configuration, workflow, or executable-document change. Apply it to the **exact final artifact**. The minimum passing grade is **A**, unless a stricter mission, protection, signed governance, regulatory, security, or production-critical requirement applies.

## Audit Evidence Requirements

For each auditable source-controlled or deployed artifact, preserve non-secret evidence containing:

| Field | Requirement |
|---|---|
| Repository and branch | Identify the source of truth and branch reviewed. |
| Base and final SHA | Bind audit results to an unchanged exact final head SHA. |
| Changed files | List all changed source, configuration, workflow, and executable-document files. |
| Artifact checksum | Record final video, binary, archive, or deployed-artifact checksum where applicable. |
| Audit provenance | Name the official OpenAI/ChatGPT audit tool, model, tool/client version, audit mode, and timestamps in Pacific and UTC. |
| Complete findings | Preserve findings, remediation rounds, tests, security scans, and evidence location. |
| Scope and rollback | State scope, material assumptions, production authorization state, and rollback method. |

Never place API keys, passwords, tokens, cookies, private keys, protected user data, or secret environment values in public evidence.

## Independent Audit Protocol

1. Request a documented **independent adversarial review** through an official ChatGPT/OpenAI auditing path. Do not call a generic AI response an audit.
2. Make the auditor review the final artifact and exact final SHA/checksum rather than implementation claims.
3. Preserve the audit prompt, complete response, run/session identifier where available, findings, test/scan results, remediation rounds, and checksum/evidence location.
4. Do not self-certify or invent a grade. The implementation agent may run the audit but cannot alter its outcome. VETS retains final approval authority.
5. If the head changes after review, report `AUDIT STALE — HEAD CHANGED` and rerun the applicable audit.

## Minimum Grade-A Decision Rubric

Assign `VETS RUBRIC GRADE: A` only when all of the following are true:

- No unresolved critical or high findings exist.
- No known secret exposure or unauthorized production mutation exists.
- No unauthorized arbitrary command-execution path exists.
- Required tests and security scans pass.
- Rollback, scope, material assumptions, and reproducible evidence are documented.
- Medium and low findings are remediated or documented with risk, compensating control, owner, and accepted disposition.
- No unresolved medium issue affects authentication, authorization, secrets, payments, production integrity, arbitrary execution, or data loss unless VETS explicitly accepts it.

If a tool does not produce a native grade, declare `AUDIT TOOL NATIVE GRADE: NONE` and assign the VETS rubric grade from preserved evidence. Do not misrepresent the rubric grade as a tool-issued grade.

## Required Decision Labels

Use exactly one of these primary statuses:

- `AUDIT STATUS: PASS — GRADE A` only for the unchanged exact final SHA/checksum.
- `AUDIT REQUIRED`
- `AUDIT STALE — HEAD CHANGED`
- `AUDIT INCOMPLETE`
- `FINDINGS REMAIN`
- `HUMAN_REVIEW_REQUIRED`
- `SOURCE_UNAVAILABLE`

Do not use `GREEN` merely because tests passed, or `PASS` merely because an AI response sounded favorable.

## Required Final Output

Return the production decision first, then the complete attestation:

```text
OVERALL STATUS: GO / NO-GO / HOLD
BIBLE AUDIT: PASS / FIX / REJECT
PRODUCTION QA: PASS / FIX / REJECT
PUBLISHING: HOLD / APPROVED BY VETS

Audit tool:
Audit model:
Tool version:
Audit timestamp Pacific:
Audit timestamp UTC:
Repository:
Branch:
Base SHA:
Final head SHA:
Changed files:
Deployed artifact SHA/checksum:
Audit mode:
Native tool grade:
VETS rubric grade:
Critical findings unresolved:
High findings unresolved:
Medium findings unresolved:
Tests:
Security scans:
Evidence path:
Head changed after audit:
Final audit status:

Failures:
Required fixes:
Rollback:
Next action recommendation:
```

Keep a sanitized summary in the Master Report. Preserve complete non-secret audit evidence in the designated evidence location.

## Grok-Bot Handoff

This public `SKILL.md` and its audit reference are the Grok-bot consumable operating instructions. Before Grok-bot evaluates a Nova package, provide the exact final assets, final checksum, applicable GitHub SHA, the scene registry, the Nova Bible audit result, and non-secret audit evidence. Grok-bot may review and report findings but must not certify its own implementation.

## Final Rule

Human review and explicit VETS approval remain mandatory for live publication. A favorable QA result clears a package for operator review; it does not authorize posting by itself.

## References

- [`VETS Standing Audit Directive`](references/VETS_STANDING_AUDIT_DIRECTIVE.md)
- [`Grok-Bot Audit Handoff`](references/GROK_BOT_AUDIT_HANDOFF.md)
- [`Nova Scene Diversity Bible`](https://github.com/jratdish1/knowledge-base/blob/main/nova/NOVA_SCENE_DIVERSITY_BIBLE.md)
- [`Nova Bible Audit Skill`](../nova-bible-audit/SKILL.md)
