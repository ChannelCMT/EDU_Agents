# Tool execution

Use deterministic tools for measurement and rendering; use models for content and visual decisions.

## Voice generation

- Send one approved semantic segment at a time to Fish Audio.
- Supply the text, tone intent, pace, pauses, and pronunciation hints from the manifest.
- Read the private voice ID from `FISH_AUDIO_VOICE_ID`; never write it to a public file.
- Save the request metadata, returned file, duration, checksum, and approval state.
- Retry only a failed segment. Do not silently switch providers or voices.

## Alignment

- Extract or use the final audio exactly as it will play in the chapter.
- Run ASR/forced alignment and preserve raw timestamps.
- Correct recognized spelling from `terminology.yaml` without changing timestamps.
- Manually check English terms, numbers, actions, and turn words.
- Fail if total token coverage is incomplete or repeated.

## HyperFrames

Pin a project version. Typical checks on Windows:

```powershell
npx.cmd hyperframes check --snapshots --samples 15 --at-transitions --json
npx.cmd hyperframes render --quality high --fps 30 --output ".\renders\chapter-v01-no-captions.mp4"
```

Run checks from the chapter project directory. Save the check JSON and contact sheet with the QA report. Do not render the full chapter while the alignment pilot is failing.

## Avatar lip-sync

- Generate lip-sync from the exact approved intro/closing audio.
- After download, inspect streams with ffprobe.
- If the clip contains audio but the composition already plays Fish Audio, strip it:

```powershell
ffmpeg -i .\avatar-with-audio.mp4 -c:v copy -an .\avatar-video-only.mp4
```

- Verify duration and mouth movement before inserting it into the animation.

## Media inspection

Inspect streams and duration:

```powershell
ffprobe -v error -show_entries format=duration -show_streams -of json .\output.mp4
```

Expected final output: one H.264 video stream, one AAC audio stream, no unintended embedded narration stream, and duration equal to the approved chapter sequence.

## Captions

- Build caption groups from final word timestamps and tone-plan pause hints.
- Validate text, length, overlap, and timing before burning.
- Burn chapter captions separately and inspect mobile-scale frames before merge.
- If only caption style changes, re-burn captions and re-merge; do not rerender animation or voice.

## Long-running jobs

- Keep the job identifier, request manifest, start time, and expected output path.
- Poll or resume the running job instead of starting a duplicate.
- When it completes, verify file existence, size, duration, streams, and content before moving to the next stage.
