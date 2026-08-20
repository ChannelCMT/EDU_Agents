# Artifact contracts

## Contents

1. Recommended project tree
2. Source-of-truth map
3. Required fields
4. Naming and versioning

## Recommended project tree

```text
project/
├─ project.yaml
├─ asset-inventory.yaml
├─ canonical-transcript.md
├─ chapter-plan.yaml
├─ visual-style.yaml
├─ RUN_STATE.yaml
├─ chapter-01/
│  ├─ SCRIPT.md
│  ├─ terminology.yaml
│  ├─ tone-plan.yaml
│  ├─ voice-manifest.yaml
│  ├─ audio_meta.json
│  ├─ word-alignment.yaml
│  ├─ semantic-anchor-plan.yaml
│  ├─ semantic-timing-manifest.yaml
│  ├─ timed-storyboard.yaml
│  ├─ layout-audit.md
│  ├─ qa-report.md
│  ├─ audio/
│  ├─ assets/
│  └─ renders/
├─ subtitle-manifest.yaml
├─ final-media-report.json
├─ publish-package.yaml
└─ PastUselessDoc/
```

## Source-of-truth map

| Decision | Source of truth | Consumers |
|---|---|---|
| Spoken content | `SCRIPT.md` | tone, TTS, captions |
| Term spelling/pronunciation | `terminology.yaml` | script review, TTS, ASR correction |
| Delivery | `tone-plan.yaml` | TTS and caption segmentation |
| Audio order/duration | `voice-manifest.yaml` + media | alignment, animation, render |
| Word times | `word-alignment.yaml` | semantic timing, captions |
| Visual meaning | `semantic-anchor-plan.yaml` | timed manifest |
| Visual seconds | `semantic-timing-manifest.yaml` | storyboard, motion implementation |
| Layout | `layout-audit.md` + source | render checks |
| Caption groups | `subtitle-manifest.yaml` | caption rendering |
| Published title/copy | `publish-package.yaml` | covers and platform post |

## Required fields

`project.yaml`:

- id, title, audience, platform, chapter_count;
- source types and rights status;
- visual style and canvas;
- approval owners;
- private/public handling.

`voice-manifest.yaml`:

- provider and public voice label (private ID via environment only);
- script version;
- ordered segments, duration, checksum, status;
- approval timestamp or status.

`semantic-timing-manifest.yaml`:

- chapter and audio version;
- cue, kind, semantic_start, visual_start;
- object, action, hold/exit and inheritance;
- early/late tolerance;
- forbidden early objects.

`semantic-beat-manifest.yaml`:

- sentence/phrase id, exact source text, word start/end, visual event id, visual start, semantic role, and voice-only justification when applicable;
- no named term, claim, contrast, cost, or risk phrase may be voice-only;
- first-30-second entries must include layer order and subtitle-band clearance evidence.

`visual-coverage-matrix.yaml`:

- one row for every caption cue;
- caption id, exact text, word evidence, visual event id(s), coverage type, and pass/fail reason;
- `coverage: voice_only` is allowed only for connective filler and must state why no visual state change is pedagogically useful.

`subtitle-manifest.yaml`:

- source final video/audio;
- caption id, exact text, start, end;
- alignment provenance and style version;
- gate summary.
- timing provenance must name `word-alignment-raw.json`; proportional timing is invalid.

## Naming and versioning

- Use stable slugs and two-digit chapter numbers: `chapter-01`.
- Append `vNN` to frozen scripts, audio sets, manifests, renders, and reports.
- Do not call files `final-final` or `new2`.
- Public templates use relative paths and environment variable names, never local user directories.
- Record current versions and gate state in `RUN_STATE.yaml`.
