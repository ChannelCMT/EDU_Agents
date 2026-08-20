---
name: course-video-pipeline
description: Turn source videos, interviews, transcripts, articles, or existing slide decks into a chaptered PPT-style animated course with rewritten narration, semantic tone planning, approved voiceover, word-level timing, synchronized motion, one-line captions, covers, and a publish package. Use when Codex needs to plan, create, repair, audit, or document a repeatable source-to-course-video workflow, especially for HyperFrames/GSAP animation, Fish Audio voice, avatar lip-sync, subtitle alignment, or multi-chapter course delivery.
---

# Course Video Pipeline

Produce course videos through evidence-backed artifacts and gates. Treat the final approved audio as timing truth; never jump from a long script directly to animation.

## Start a project

1. Read `references/workflow.md` for the end-to-end sequence.
2. Read `references/artifact-contracts.md` and create the required artifacts.
3. Copy `assets/project-template/` manually, or run:

```powershell
python scripts/init_course_project.py --output <project-path> --title "<course title>" --chapters 5
```

4. Lock audience, platform, chapter count, visual style, and approval checkpoints in `project.yaml`.
5. Validate structure before producing media:

```powershell
python scripts/validate_course_video.py <project-path> --structure-only
```

## Execute the fixed sequence

1. Inventory source media and copyright/privacy constraints.
2. Produce a canonical transcript, source timecodes, and terminology list.
3. Convert the source into a teaching arc and one canonical `SCRIPT.md` per chapter.
4. Create `tone-plan.yaml`: intention, pace, pauses, emphasis, breath points, and pronunciation for every segment.
5. Generate voice segments and obtain explicit human approval. Keep one voice per sentence.
6. Align the final audio at word or critical-phrase level. Do not estimate animation seconds before this step.
7. Create semantic anchors, then a timed manifest, then the storyboard and layout audit.
8. Implement and review the highest-risk 15–20 seconds before the whole chapter.
9. Implement the full chapter only from approved manifests. Run layout, runtime, motion, contrast, media-stream, and human listen/watch checks.
10. Render and approve chapters separately.
11. Generate captions from final chapter audio, burn captions, merge chapters, and verify media streams.
12. Produce 4:3 and 3:4 covers, publish copy, and a release manifest.
13. Record platform feedback as a new checkable Harness rule.

Read `references/tool-execution.md` when running TTS, alignment, HyperFrames, avatar lip-sync, FFmpeg, or final media verification.

## Apply non-negotiable gates

- Read `references/harness.md` before voice, storyboard, animation, caption, avatar, cover, or release work.
- Use one cue for one primary visual/state change.
- Keep visual entry within `-0.15s/+0.12s` of its spoken semantic anchor.
- Keep the subtitle safe band `y=900..1080`; key teaching content ends above `y=870`.
- Use PPT title text at least 54px, body text at least 24px, and key node/card text at least 26px on 1920×1080.
- Use one-line captions of 5–14 visible characters, exact spoken order, target start offset `-50ms`, and maximum word alignment error `80ms`.
- Use a genuinely translucent subtitle layer; do not hide layout conflicts with an opaque caption box.
- Check every external lip-sync video for an embedded audio stream. The final mix contains exactly one narration stream.
- Preserve UTF-8 and use relative paths in public artifacts.

## Route work deliberately

Read `references/role-routing.md` when assigning models or tools.

- Use Luna Ultra for content reasoning, tone, semantic mapping, caption segmentation, and audits.
- Use Terra High for approved-manifest implementation, motion/layout repair, rendering, and media diagnosis.
- Use SOL only after the same semantic conflict fails twice; request conflict, evidence, correct order, and timing window—not a chapter rewrite.
- Use deterministic tools for transcription, TTS, alignment, rendering, media streams, and long-running jobs.
- Keep human approval for script, voice, pilot, chapter, and publish decisions.

## Repair with the minimal Loop

1. Record timestamp, category, evidence, expected behavior, and actual behavior.
2. Find the source-of-truth artifact in `references/artifact-contracts.md`.
3. Repair the smallest artifact: phrase, anchor, object, caption group, or media track.
4. Re-render scene, then chapter, then full video only if required.
5. Run machine checks, targeted frame/audio inspection, and human review.
6. Freeze the passing version and archive failed work under `PastUselessDoc`.

## Learn from the completed example

Read `references/five-chapter-case-study.md` when diagnosing repeated timing mismatches, mixed-language pronunciation, old-layer competition, subtitle occlusion, small mobile text, cover overlap, or duplicate lip-sync audio.

## Validate before handoff

Run:

```powershell
python scripts/validate_course_video.py <project-path>
```

Do not declare delivery complete until the chapter gates, subtitle gate, media report, cover checks, public sanitization, and human approvals pass.
