# Semantic QA report

## Gate result

- Chapters: 5
- Semantic anchors: 31/31 pass
- Visual entry rule: `semantic_start - 0.15 <= visual_start <= semantic_start + 0.12`
- Caption entry: -50 ms relative to the checked cue start
- Caption layout: one line, 5–14 visible characters; `容易跑偏` is retained as an exact four-character spoken phrase
- Static gap limit: 1.4 s

## Canonical English terms

The display layer uses the canonical spellings `ReAct`, `Plan and Execute`, `Multi-Agent`, `Route+Skill`, `Blackboard`, `Graph Workflow`, `Coordinator`, `Planner`, `Executor`, and `Reviewer`. ASR variants such as “Reactor”, “Rooter”, or “Reveal” are never copied into the PPT, animation, or captions.

## Visual/audio alignment notes

- Chapter 1 introduces the two-axis selection coordinate system before revealing the evolution line.
- Chapter 2 starts ReAct visuals at the spoken transition, then reveals the Reason–Action–Observe loop.
- Chapter 3 reveals Coordinator and role cards at the Multi-Agent handoff, with failure handling at the closing sentence.
- Chapter 4 reveals Skill cards during the route sentence and the shared-state board during the Blackboard sentence.
- Chapter 5 delays branch/retry visuals until the Graph Workflow sentence and staggers the seven architecture nodes across the evolution explanation.
