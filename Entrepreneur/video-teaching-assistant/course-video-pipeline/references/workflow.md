# End-to-end workflow

## Contents

1. Production model
2. Fourteen execution stages
3. Human approval points
4. Version and archive policy

## Production model

The workflow has three distinct layers:

1. **Meaning**: transcript, teaching structure, script, tone, terminology.
2. **Time and visuals**: approved audio, word alignment, semantic anchors, storyboard, animation.
3. **Distribution**: captions, merge, covers, copy, release package.

Never let a downstream layer invent an upstream decision. Animation does not rewrite the script; captions do not guess missing words; covers do not invent a different title.

## Execution stages

### 1. Intake and constraints

Collect source video/audio/text, existing PPT, reference style, audience, platform, target duration, aspect ratio, and rights/privacy status. Produce `project.yaml` and `asset-inventory.yaml`.

Gate: the owner explicitly approves the audience and platform. If a third-party source is used, store only notes, timecodes, and licensed assets; do not copy protected media into a public repository.

### 2. Canonical transcript

Run ASR, then manually correct terms, names, numbers, and section boundaries. Keep source timecodes separate from the rewritten course script.

Gate: every source section is represented; the terminology file has one approved spelling per term.

### 3. Course architecture

Convert the source into chapters. Each chapter must have one learner problem, one core result, and one visible proof or application. For a five-chapter explainer, use a progression such as problem → distinction → system → constraints → application.

Gate: no chapter exists only to repeat the previous one, and each conclusion supports the next chapter.

### 4. Script rewrite

Write spoken Chinese rather than slide prose. Keep one primary conclusion per paragraph. Translate vague preferences into checkable rules with object, pass condition, failure handling, and evidence/rollback.

Gate: the owner approves a single versioned `SCRIPT.md` for each chapter.

### 5. Tone and pronunciation planning

For each spoken segment, record intent, emotional contour, pace, pause duration, emphasis words, breath points, and English pronunciation. Prefer one bilingual-capable voice for a complete sentence. If a term remains wrong, regenerate the smallest segment or use an approved recording; do not switch voices mid-sentence by default.

Gate: Mandarin is natural, English terms are understood, and the planned pauses support later caption boundaries.
The plan is sentence-level: every sentence has a delivery intention and a visual-sync target. Do not pass a chapter with only a global style adjective.

### 6. Voice generation

Generate segmented audio from the approved script and tone plan. Save provider, voice label, model/version, segment order, checksum, duration, and approval status. Keep IDs and training audio private.

Gate: the final audio is frozen. All later timing derives from this version.

### 7. Word/phrase alignment

Align the final audio to the exact approved script. Correct ASR spellings using the terminology file while preserving actual timing. Manually inspect English terms, numbers, and transitions.

Gate: every spoken token is covered exactly once and the total timeline equals the final audio duration.

### 8. Semantic mapping

Create anchors of four kinds: `segment`, `term`, `action`, and `turn`. Map each cue to one visual object/state change. First write anchors without seconds, then fill real timing from alignment.

Gate: every important cue has a visual or is explicitly marked `voice_only`; every visual action has a cue.
The evidence is stored in `semantic-beat-manifest.yaml` and `visual-coverage-matrix.yaml`, not only in a chapter summary.

### 9. Storyboard and layout

Write `semanticStart`, `visualStart`, enter/hold/exit, inheritance, and forbidden early objects. Divide the canvas into title, main structure, auxiliary cards, conclusion, and reserved subtitle band before positioning elements.

Gate: timing windows, text sizes, bounding boxes, and subtitle clearance pass.

### 10. Alignment pilot

Choose the 15–20 seconds with the densest terminology, state changes, or arrows. Render this exact range. Check that the visual subject matches the spoken subject and that later concepts do not appear early.

Gate: human approval. Do not build the chapter while the pilot is failing.

### 11. Full chapter implementation and render

Implement only from approved manifests. Keep motion seek-safe and deterministic. Run runtime, layout, motion, contrast, text-size, UTF-8, media-stream, snapshot, and human listen/watch checks.

Gate: render and approve each chapter separately. Archive superseded outputs.

### 12. Captions and merge

Generate captions from the final chapter audio—not from the draft script. Segment at tone-plan pauses and complete semantic boundaries, then enforce 5–14 visible characters and one line. Burn chapter captions and merge only approved chapter files.

Gate: exact text sequence, timing error ≤80ms, mobile readability, H.264/AAC, one narration stream.
Any caption builder that allocates time by character proportion fails this gate; word-level timing evidence is mandatory.

### 13. Cover and publish package

Create 4:3 and 3:4 covers with the same title/copy source. Check actual visual bounding boxes, safe margins, unexpected wrapping, and platform cropping. Package final MP4, covers, description, hashtags, pinned comment, and release manifest.

Gate: owner approves the full package and public sanitization passes.

### 14. Release learning Loop

Convert platform feedback into checkable Harness rules. Example: “mobile text is small” becomes numeric minimum type sizes and a 50% preview requirement. Apply new rules to future work, not just the published video.

## Human approval points

Require explicit approval after:

- audience/platform lock;
- chapter plan;
- script;
- voice;
- 15–20 second pilot;
- each chapter;
- final captions/merge;
- cover and publish package.

## Version and archive policy

- Never overwrite a frozen output.
- Use `vNN` in script, audio, manifest, render, and report names.
- Move failed or superseded work to `PastUselessDoc/<date>-<reason>/` with a short index.
- Keep current source, final audio, current manifests, current render, and final reports outside the archive.
