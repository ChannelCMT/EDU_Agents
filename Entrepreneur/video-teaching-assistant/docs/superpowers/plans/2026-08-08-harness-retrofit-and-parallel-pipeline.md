# Harness Retroﬁt and Parallel Chapter Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prevent weak hooks, visual overlaps, and false-passing subtitle alignment gates, while allowing independent chapters to run in parallel after shared inputs are frozen.

**Architecture:** Keep content and final audio as shared upstream truth. Add source-level and rendered-frame gates before chapter rendering, normalize segment-local word timestamps before cue selection, and represent chapter work as fan-out/fan-in jobs with immutable per-chapter artifacts.

**Tech Stack:** YAML workflow manifests, Python audit scripts, HyperFrames/GSAP HTML, PyAV, Playwright frame capture.

## Global Constraints

- Final approved voice remains the timing source of truth.
- First five seconds must be understandable without prior knowledge of ReAct or Multi-Agent.
- Every subtitle cue must carry global word evidence and be within 80ms of that evidence.
- Every chapter must reserve the subtitle safe band and pass rendered-frame overlap checks.
- Chapter fan-out is allowed only after script, tone plan, voice, alignment, and pilot gates are frozen.

### Task 1: Record the failure evidence

**Files:**
- Create: `docs/06_复盘与并行生产.md`
- Create: `content/harness-lessons-v06.yaml`

- [x] Document the three reproduced failures: jargon-first opening, source-only layout checks, and segment-local word timestamps.
- [x] Map each failure to the exact artifact boundary and the gate that incorrectly passed it.
- [x] Document the safe parallel fan-out/fan-in boundary and prohibited shared writes.

### Task 2: Strengthen content and visual Harness rules

**Files:**
- Modify: `workflow/master-harness.yaml`
- Modify: `workflow/course-video-workflow.yaml`
- Modify: `workflow/role-routing.yaml`

- [x] Add a first-five-second hook gate: audience tension first, unfamiliar architecture terms delayed, spoken copy and visual title must match.
- [x] Require rendered intermediate-frame checks, DOM bounding boxes, minimum font sizes, and subtitle-band clearance; source regex checks alone are insufficient.
- [x] Add `parallel_groups`, `join_barriers`, artifact locks, and retry scope to the workflow and role routing.

### Task 3: Make subtitle alignment fail closed

**Files:**
- Modify: `projects/agent-architecture-7-patterns/tools/build_word_aligned_captions.py`
- Modify: `projects/agent-architecture-7-patterns/tools/audit_harness_gates.py`
- Create: `projects/agent-architecture-7-patterns/tools/audit_caption_alignment.py`

- [x] Normalize segment-local words to global time before selecting cue evidence.
- [x] Reject non-monotonic words, overlapping cues, first-cue starts after 10ms, missing evidence, and cue/evidence deltas over 80ms.
- [x] Emit a machine-readable report with chapter, cue id, raw segment, normalization mode, and failure action.

### Task 4: Add visual overlap and opening-hook gates

**Files:**
- Create: `projects/agent-architecture-7-patterns/tools/audit_rendered_layout.py`
- Modify: `projects/agent-architecture-7-patterns/tools/audit_harness_gates.py`

- [x] At fixed checkpoints, inspect rendered DOM boxes for title, subtitle, axes, graph panels, and caption band.
- [x] Reject any forbidden intersection, off-canvas box, font below floor, or caption that hides a key object.
- [x] Add a hook checkpoint at 0.0–5.0 seconds and require the intended opening text to be visible in the contact sheet.

### Task 5: Verify and publish the revised process

**Files:**
- Modify: `docs/01_端到端制作流程.md`
- Modify: `docs/02_Harness与返工闭环.md`
- Modify: `README.md`

- [x] Run the caption, Harness, layout, and project validators against the existing five-chapter case.
- [x] Verify that the revised gates fail on a deliberately local-timestamp fixture and pass on the current normalized artifacts.
- [x] Record the parallel schedule and handoff rules in the public workflow documentation.
