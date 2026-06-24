---
name: nova-bible-audit
description: Audit any Nova Reign image prompt, video prompt, still frame, render, or final video asset against the locked Nova Bible and production QA rules.
---

# Nova Bible Audit Skill

Use this skill to audit any Nova Reign image prompt, video prompt, still frame, render, or final short-form video asset.

## Mission

Determine whether the asset is approved for production, needs fixes, or must be rejected and regenerated.

Return one of only three final ratings:

- PASS
- FIX
- REJECT

---

## Locked Nova Bible

Nova Reign must appear as:

- Lean athletic toned fit woman
- Mixed Latina/Black ethnicity
- Warm medium brown skin
- Late 20s
- Long dark wavy/curly voluminous hair past shoulders
- Hazel amber golden-brown eyes
- High cheekbones
- Full lips
- Soft natural brows
- Warm confident smile or confident warrior expression
- Strong jawline
- Always wearing military dog tags
- Photorealistic, cinematic, high detail
- Vertical 9:16 format for shorts content
- SFW public-platform safe

---

## Non-Negotiable Tattoo Orientation Rule

This is the highest-priority rule.

- LEFT side of image/frame = Nova's right arm.
- The arm on the LEFT side of the image/frame must show the full American flag tattoo sleeve.
- Tattoo sleeve must include:
  - Bald eagle at shoulder
  - Stars and stripes
  - "1776"
  - "E Pluribus Unum"
- RIGHT side of image/frame = Nova's bare arm.
- The arm on the RIGHT side of the image/frame must be completely bare:
  - no tattoos
  - no partial sleeve
  - no markings
  - no mirrored tattoo
  - no accidental second sleeve

If tattoo orientation is wrong, return REJECT.

If both arms have tattoos, return REJECT.

If the tattoo is missing from the LEFT side of frame, return REJECT.

If the RIGHT side of frame has any tattoo or marking, return REJECT.

---

## Required Audit Checks

Check the asset for:

1. Tattoo orientation
2. Tattoo content accuracy
3. Hazel amber golden-brown eyes
4. Athletic toned build
5. Warm medium brown skin
6. Long dark wavy/curly hair
7. Dog tags visible
8. Face consistency with Nova Bible
9. Photorealistic cinematic style
10. Vertical 9:16 framing
11. SFW compliance
12. No distorted hands, arms, anatomy, or face
13. No misspelled tattoo text
14. No unwanted watermarks
15. No platform-policy concerns
16. No accidental real-person impersonation risk

---

## Rating Rules

Return PASS only if all locked requirements are satisfied.

Return FIX if the asset is mostly correct but has minor repairable issues, such as:

- captions need cleanup
- lighting needs improvement
- crop/framing needs adjustment
- dog tags are partially hidden but can be corrected
- prompt needs more detail before generation

Return REJECT if any non-negotiable Bible rule fails, especially:

- tattoo on wrong side
- tattoo on both arms
- missing tattoo sleeve
- bare arm not bare
- wrong eye color
- no dog tags
- not Nova-like
- NSFW issue
- distorted anatomy
- non-photorealistic result when photorealism was required

---

## Required Output Format

Always output exactly this structure:

```
AUDIT RESULT:
PASS / FIX / REJECT

ASSET TYPE:
Image prompt / Video prompt / Still frame / Render / Final video / Unknown

ISSUES FOUND:
- List each issue clearly.
- If no issues, write: None.

BIBLE CHECKLIST:
- Tattoo LEFT side sleeve:
- RIGHT side bare arm:
- Hazel eyes:
- Athletic build:
- Dog tags:
- Hair:
- Skin tone:
- Photorealistic:
- Vertical 9:16:
- SFW:

EXACT CORRECTION PROMPT:
Provide a copy/paste correction prompt that fixes the issues.

PRE-PUBLISH RECOMMENDATION:
State whether the asset may proceed to Grok, Foxy.AI, HeyGen, Kling, fish.audio, ffmpeg, scheduling, or must be regenerated.

FINAL DECISION:
PASS / FIX / REJECT
```
