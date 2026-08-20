# Role routing

## Human owner

Own subjective and irreversible choices: audience, script, voice, pilot, chapter approval, cover, and publication. Ask for approval only at these checkpoints or when rights/authorization are missing.

## Luna Ultra

Use for content understanding, chapter structure, natural Chinese rewrite, tone planning, semantic anchors, storyboard reasoning, caption segmentation, and QA. Luna can start and inspect long-running jobs but should not be the execution engine for prolonged rendering or external API waits.

Expected outputs are plans, manifests, audits, and precise minimal repair lists.

## Terra High

Use after manifests pass. Implement HTML/GSAP/HyperFrames, complex graph/arrows, audio hookup, layout corrections, deterministic rendering, media-stream diagnosis, and minimal engineering fixes.

Terra must not silently change script meaning or invent timing.

## SOL

Use only after the same semantic conflict fails twice or two plausible interpretations remain. Provide the raw audio phrase, word times, current manifest, frame evidence, and failed expectation. Request only:

1. conflict location;
2. evidence words;
3. correct visual order;
4. recommended timing window.

Do not ask SOL to rewrite a whole chapter or replace measurement with reasoning.

## Deterministic toolchain

Use tools for transcription, TTS, alignment, lip-sync, animation runtime, media encoding, and stream inspection. Save requests, versions, outputs, durations, and errors. Long-running status is expected; resume and verify instead of declaring a task stopped merely because no new output appeared.

## Failure routing

| Failure | First return point | Do not do |
|---|---|---|
| Wrong claim or audience | script | patch animation text only |
| Wrong pronunciation | terminology/tone/voice segment | slow the entire video |
| Visual late/early | word alignment + semantic timing | add arbitrary page delay |
| Overlap/overflow | layout audit + scene source | shrink below font minimum |
| Duplicate voice | media stream mapping | regenerate all narration |
| Caption wrong words | alignment/canonical transcript | manually hide mismatch |
| Caption bad break | tone pauses + segmentation | split only by character count |
| Cover overlap | bounding boxes | hide with opacity or crop |
