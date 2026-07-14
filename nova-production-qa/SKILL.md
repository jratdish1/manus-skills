---
name: nova-production-qa
description: Final Quality Assurance check on the complete video package before posting. Enforces V2 Motion-First Pipeline and Scene Diversity rules.
---

# Nova Production QA

Perform a final Quality Assurance check on the complete video package before posting.

## V2 PIPELINE RULES (MANDATORY)
1. **NO STATIC PHOTO AVATARS.** The pipeline MUST use a video-to-video approach: generate an 8-second motion base clip (with breathing/human movement) first, then apply HeyGen lipsync over the moving video.
2. **CLEAN AUDIO.** All voiceover audio MUST be trimmed at the head (remove first 0.1s artifact), faded in (50ms), and normalized before HeyGen ingestion to prevent echo/feedback on first play.

## SCENE DIVERSITY RULE (MANDATORY)
- **NO BACKGROUND REUSE.** Every episode MUST have a unique background, activity, and content environment.
- Check the Nova Scene Diversity Bible (Ep. 1-30). If the background/scene matches a previous episode, REJECT and regenerate.

## QA Checklist

### 1. Visual (Refer to nova-bible-audit for deep character check)
- [ ] Tattoo orientation is correct (LEFT frame = Right arm sleeve).
- [ ] 9:16 Vertical format.
- [ ] Lip-sync matches audio.
- [ ] Body movement is natural (breathing, subtle shifts) — NOT robotic/static.
- [ ] Background is unique and adheres to the Scene Diversity rule.

### 2. Audio
- [ ] Voice matches Nova's spec.
- [ ] Audio is clear, no clipping, NO ECHO/POP at the start.
- [ ] Pacing feels natural.

### 3. Metadata
- [ ] Title is punchy and platform-safe.
- [ ] Description includes CTA/Question.
- [ ] Hashtags are present and relevant.

## Always output:
1. OVERALL STATUS: GO / NO-GO
2. Failures (if any)
3. Required Fixes
