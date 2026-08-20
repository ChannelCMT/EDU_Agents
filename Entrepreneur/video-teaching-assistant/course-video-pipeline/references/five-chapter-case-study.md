# Harness Engineering five-chapter case study

## Contents

1. Final structure
2. Chapter lessons
3. Cross-project rules learned

## Final structure

| Chapter | Teaching result | Visual logic |
|---|---|---|
| 1. Why Harness | The same model can behave differently because of the surrounding work system | question → contrast → system → evidence → human work shifts |
| 2. Prompt, Context, Harness | Prompt controls expression, Context controls information, Harness controls work | nested concepts → boundaries → progressive disclosure |
| 3. Loop and components | Reliability needs execution, feedback, verification, and recovery | control loop → failure path → six components |
| 4. Executable constraints | Entry maps, evidence rules, architecture, and permissions make experience executable | bad rule → directory/map → evidence → dependency boundary |
| 5. Minimal landing | Start with a low-risk real task and expand autonomy with evidence and rollback | L1–L6 → minimal directory → entrepreneur example → acceptance |

Final merged duration was about 441.6 seconds. Chapters were approved separately and then captioned and merged.

## Chapter lessons

### Chapter 1: voice quality before animation timing

Several voice variants exposed dialect, English accent, slow English inserts, and unnatural splices. The stable result used one Chinese technology-explainer voice for complete sentences, a semantic tone plan, and a locked pronunciation list. The chapter intro used an avatar briefly, then moved to graphics.

Rule learned: one sentence uses one approved voice; fix a bad word at terminology/tone/segment level before rebuilding animation.

### Chapter 2: page order is not semantic order

The 3–20 second section failed repeatedly because the animation was designed as three parallel page concepts while the narration introduced them sequentially. Estimated timing and two overlapping legacy timelines made later concepts appear early.

The fix used one inherited semantic canvas: Prompt appears first, Context grows around it, and Harness appears only when spoken. Word-level anchors replaced page-duration guesses.

Rule learned: choose the current spoken subject as the visual subject; remove competing legacy timelines; validate the hardest 15–20 seconds first.

### Chapter 3: layout and semantic gates are separate

Text boxes overlapped and a later sequence around 31 seconds did not match speech. Treating this as one generic animation issue caused unnecessary rework.

The fix separated layout bounding-box checks from semantic timing checks, then repaired arrows and state order independently.

Rule learned: a clean layout can still be semantically wrong, and correct timing can still be unreadable. Both gates must pass.

### Chapter 4: English terms need measured word times

Title spacing and lower-left elements collided, while `Types` and `Config` appeared after they were spoken. Tightening review without better timing data was not enough.

The fix used actual word times for English nodes, preserved font minimums, and changed layout rather than shrinking text.

Rule learned: English terms, numbers, and turns need manual alignment checks; never assign them a fixed interval.

### Chapter 5: audience consistency and media streams

The script drifted from entrepreneur-focused teaching into a university-student example. The closing avatar also carried its own audio while the page separately played Fish Audio, producing duplicate narration.

The fix removed the audience drift, centered the entrepreneur use case, shortened the closing to under eight seconds, regenerated lip-sync with the exact closing audio, and stripped the external clip audio before composition.

Rule learned: audience is a content gate; every external avatar clip receives a media-stream gate; the final mix contains one narration stream.

## Cross-project rules learned

- Final audio is the only timing truth.
- Stronger reasoning does not replace word alignment or deterministic media checks.
- Plan → align → pilot → implement → audit is cheaper than script → full render → rework.
- Mobile publication needs larger PPT text, one-line captions, a translucent caption layer, and a reserved subtitle band.
- Caption breaks must follow semantic and tone pauses, not just character count.
- Publishing is part of the pipeline: covers, copy, crop previews, media report, and feedback belong in the Harness.
