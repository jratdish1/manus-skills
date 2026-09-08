# Manus Skills: Nova Bootcamp Series 1

This public repository contains concise, Manus-compatible skills for the Nova Reign Bootcamp video-production pipeline. It contains reusable operating instructions only. **It must never contain secrets, tokens, API keys, private URLs, production credentials, cookies, passwords, or protected user data.**

## Available Skills

| Order | Skill | Purpose |
|---:|---|---|
| 1 | [`nova-bible-audit`](nova-bible-audit/SKILL.md) | Audits any image/video prompt or asset against the locked Nova Bible, including the strict tattoo-orientation rule. |
| 2 | [`brag-nova`](brag-nova/SKILL.md) | Generates status reports and production brag documents. |
| 3 | [`nova-shorts-package`](nova-shorts-package/SKILL.md) | Formats complete script and metadata packages for YouTube Shorts using the E-A-S-Y framework. |
| 4 | [`nova-caption-pack`](nova-caption-pack/SKILL.md) | Generates tailored captions for YouTube Shorts, TikTok, Instagram Reels, Fanvue, and X. |
| 5 | [`nova-production-qa`](nova-production-qa/SKILL.md) | Performs the final motion, audio, visual, metadata, evidence, and VETS audit-gate review before publication. |

## Audit and Grok-Bot Review

The `nova-production-qa` skill embeds the **VETS Standing Audit Directive**. It requires exact-artifact evidence, an independently requested adversarial audit, non-secret evidence preservation, and a minimum **VETS rubric grade of A** unless a stricter gate applies.

| Reference | Purpose |
|---|---|
| [`VETS Standing Audit Directive`](nova-production-qa/references/VETS_STANDING_AUDIT_DIRECTIVE.md) | Governing requirements for attributable, reproducible, exact-artifact audit evidence and final reporting. |
| [`Grok-Bot Audit Handoff`](nova-production-qa/references/GROK_BOT_AUDIT_HANDOFF.md) | Non-secret handoff checklist and paste-ready advisory-review prompt for a Grok-bot review. |
| [`Exact Reference Binding`](nova-production-qa/references/EXACT_REFERENCE_BINDING.md) | Requires a commit SHA and file checksum for every governing Nova Bible, scene registry, prompt, and source document. |
| [`Production Authorization and Evidence`](nova-production-qa/references/PRODUCTION_AUTHORIZATION_AND_EVIDENCE.md) | Defines the private, checksum-bound VETS approval record, evidence retention, and rollback gate required before a live mutation. |

> A public GitHub file is accessible to a Grok-bot or other reviewer only when that bot is actually configured with access to this repository or is provided the public commit URL. These documents do not authorize publishing, scheduling, secret handling, or self-certification. Explicit VETS approval remains mandatory for live publication.

## How to Use

Import the repository into a Manus Project from the **Skills** tab using:

```text
https://github.com/jratdish1/manus-skills
```

For an exact, immutable review handoff, use the commit-pinned GitHub URLs emitted in the final verification report rather than a branch URL.
