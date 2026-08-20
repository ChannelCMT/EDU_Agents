# Quality Harness

## Contents

1. Content and voice gates
2. Semantic timing gate
3. Layout and motion gate
4. Avatar and media gate
5. Caption gate
6. Cover and release gate

## Content and voice gates

- Keep exactly one approved script per chapter.
- Use conversational narration; a slide title is not automatically a spoken sentence.
- Describe every requirement with check object, pass standard, failure action, and evidence/rollback.
- Lock English spelling and pronunciation before TTS.
- Keep one voice per sentence. Regenerate only the failed segment.
- The final approved voice track is the timing source of truth.
- Do not lock animation seconds before `voice-manifest`, `audio_meta`, and word alignment exist.
- `tone-plan.yaml` must contain one row per spoken sentence. Each row records intent, energy, pace, emphasis, pause, breath, pronunciation, and the visual event it drives. A generic chapter-level style adjective is not sufficient evidence.

## Semantic timing gate

Each anchor contains:

```yaml
id: "A01"
cue: "Harness"
kind: "term"
semantic_start: 12.420
visual_start: 12.320
object: "term-card-harness"
action: "fade-in-and-highlight"
hold_until: 15.800
exit: "inherit"
forbid_before: ["harness-definition"]
```

Pass when:

```text
semantic_start - 0.15 <= visual_start <= semantic_start + 0.12
```

Also enforce:

- one cue → one primary visual/state change;
- a `turn` cue changes state before the next content group;
- no semantically static gap longer than 1.4 seconds;
- later terms/definitions do not appear early;
- old timelines and hidden layers cannot compete with the current scene.
- Create `semantic-beat-manifest.yaml` at sentence/phrase level. A chapter-level anchor list is only an index; it cannot be the sole timing evidence.
- Create `visual-coverage-matrix.yaml` so every caption cue maps to a visible object/state change or an explicit `voice_only` reason. Named terms, claims, contrasts, and cost/risk statements may not be marked `voice_only`.
- Run a dedicated first-30-second layer audit. It must check entry order, off-screen objects, subtitle-band clearance, and unmapped speech gaps before full-chapter rendering.

## Layout and motion gate

For 1920×1080:

- title ≥54px;
- body/card explanation ≥24px;
- key node/card title ≥26px;
- key content ends above y=870;
- subtitle band is y=900..1080;
- at most one primary structure and three auxiliary cards per scene;
- no text overflow, content overlap, off-canvas panel, card-piercing arrow, or accidental crop.

Check initial, entering, holding, transition, and exit frames. A final still image passing does not prove the animation passes.

Use UTF-8 for HTML/JSON/YAML. After automated rewrites, inspect Chinese text and literal `<span>` leakage before rendering.

## Avatar and media gate

- Default avatar use is a 3–8 second chapter intro or a brief closing.
- Lip-sync audio must be the exact final approved audio segment.
- Inspect every generated MP4 for embedded audio before composition.
- If the page already plays Fish Audio, strip or mute LatentSync/HeyGen clip audio.
- Final chapter and final merge contain one narration stream only.
- Verify file duration and streams after every long-running external job.

## Caption gate

- Source captions from final audio alignment.
- Caption start/end must be derived from `word-alignment-raw.json` word spans. Character-weight or proportional segment timing is forbidden.
- Every cue stores alignment evidence (`word_start`, `word_end`, source segment, and error). A cue without word evidence fails even if its chapter duration looks correct.
- Preserve 100% spoken word order; only punctuation and approved English capitalization may change.
- Show one line and 5–14 visible characters.
- Prefer a complete sentence, pause, semantic phrase, then hard length limit.
- Do not split English words or leave a verb without its object.
- Target start is 50ms before speech; maximum word alignment error is 80ms.
- Use 52px white bold text (minimum 48px) on a semi-transparent navy layer with a light-blue translucent edge.
- The underlying PPT must remain visible, but the subtitle safe band still must be empty of critical content.
- Review original size and a mobile/50% preview.

## Cover and release gate

- Produce 4:3 and 3:4 covers.
- Check true visual bounding boxes, including glow, shadow, stroke, and arrow heads.
- Fail any text/graphic, graphic/border, text/accent-bar, or card/arrow intersection.
- Keep the rightmost graphic at least 56px from the border on a 1440×1080 reference canvas.
- Verify exact title copy and unexpected wrapping.
- Preview at 100% and with platform crop.
- Public package excludes secrets, voice training media, avatar source media, large intermediate renders, and unlicensed assets.
