# Chapter 1 layout audit

- Canvas: 1920 × 1080
- Subtitle safe band: y=900..1080
- Key content ceiling: y<870
- Title minimum: 76 px; body minimum: 25 px; key node minimum: 27 px

| Check | Evidence | Result |
|---|---|---|
| Runtime | HyperFrames strict check | PASS |
| Layout / bounds | HyperFrames strict check | PASS |
| Motion / semantic entry | semantic-anchor-plan.yaml | PASS |
| Contrast | HyperFrames strict check | PASS |
| Text size | generator style tokens | PASS |
| UTF-8 | local frame inspection | PASS |
| Media streams | chapter MP4 H.264 + AAC | PASS |
| Caption occlusion | translucent bottom safe band | PASS |
