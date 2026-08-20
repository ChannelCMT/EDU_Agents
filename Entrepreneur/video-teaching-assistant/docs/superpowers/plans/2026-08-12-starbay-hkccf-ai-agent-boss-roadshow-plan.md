# Starbay HKCCF AI Agent Boss Roadshow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a separate 13-slide, 15-minute Hong Kong Computer & Communications Festival PowerPoint that tells Starbay's six-month AI Native transformation story and converts enterprise owners to the 29–30 August 2026 AI Builder Camp.

**Architecture:** Use the existing 10-slide roadshow PPTX as the sole visual template. Import it with `@oai/artifact-tool`, inspect every source slide, duplicate mapped source slides into a 13-slide starter deck, then edit inherited text and image elements in place. Keep slide copy, speaker notes, element IDs, sources, image prompts, and QA evidence in small build files so content, template fidelity, visual assets, and verification can be reviewed independently.

**Tech Stack:** JavaScript ES modules, `@oai/artifact-tool`, bundled Node.js/Python presentation utilities, PowerPoint template-following scripts, built-in ImageGen/Image 2, PowerShell, PowerPoint PPTX.

## Global Constraints

- Approved design spec: `Course1/HarnessEngineeringPPT/courseVedio/docs/superpowers/specs/2026-08-12-starbay-six-month-ai-agent-transformation-roadshow-design.md`.
- Read-only source deck: `Course1/HarnessEngineeringPPT/AIBuilderCampRoadshow/AI_Builder_Camp_15min_Roadshow_2026-08-29_30.pptx`.
- Preserve the source deck unchanged; verify its SHA-256 before and after implementation.
- Final deck: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/Starbay_AI_Agent_Boss_HKCCF_15min_2026-08-29-30.pptx`.
- Visible copy is Traditional Chinese; speaker notes are natural Cantonese.
- Use 「半年」 for the transformation period; the old period wording must not appear in visible slide copy.
- Use exactly these business categories: 網站建設、視覺設計、活動承辦、AI 實訓.
- Preserve the three approved AI Native principles and the approved OPC definition verbatim.
- Use the exact boundary sentence: 「灣星連接港科大（廣州）科研場景開展 AI 實訓。」
- Any visit statement must also say it is an activity arrangement, not a university course or professor-taught class, and is subject to the event notice.
- The Agent-population statement is a forecast, not a current global statistic.
- Main CTA is registration for AI Builder Camp; school, youth, and enterprise cooperation is secondary.
- Use at least six different Image 2/ImageGen technology visuals. Generated visuals must never impersonate clients, real events, or HKUST(GZ) documentary photography.
- Do not invent efficiency, revenue, client, advertising-return, labour-hour, or Agent-count metrics.
- Use `@oai/artifact-tool` from `.mjs` files. Do not use `python-pptx`, direct OOXML mutation, or a fresh theme-matched rebuild.
- Template following is mandatory: every output slide maps to a source slide and edits inherited elements.
- Keep all intermediates under `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/`; only the final PPTX sits one directory above.
- The workspace has no Git metadata. Do not initialize a repository; replace commit steps with explicit checkpoint entries in `build/qa-ledger.txt`.

## File Structure

```text
Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/
├── Starbay_AI_Agent_Boss_HKCCF_15min_2026-08-29-30.pptx
└── build/
    ├── content.json                 # 13-slide copy, notes, timing, sources, asset names
    ├── edit-plan.json               # output-slide roles mapped to inherited element IDs
    ├── template-audit.txt           # source layouts, typography, chrome and placeholder rules
    ├── template-frame-map.json      # 13 output slides mapped to source slides
    ├── deviation-log.txt            # approved departures from inherited source elements
    ├── template-starter.pptx        # duplicated source-slide starter deck
    ├── image-prompts.txt             # final prompt and mode for every generated image
    ├── source-notes.txt              # URLs, local asset provenance and source-deck hash
    ├── qa-ledger.txt                 # task checkpoints and per-slide QA findings
    ├── validate-content.mjs          # deterministic content and timing checks
    ├── preview-batch.mjs             # renders one slide-module batch for review
    ├── deck.mjs                      # composes modules, adds notes, renders and exports PPTX
    ├── lib/
    │   └── deck-helpers.mjs          # ID resolution, text/image replacement, notes, export helpers
    ├── slides/
    │   ├── slides-01-05.mjs          # hook and Starbay transformation
    │   ├── slides-06-10.mjs          # Agent service model and training entry points
    │   └── slides-11-13.mjs          # HKUST(GZ) boundary, two-day camp and CTA
    ├── tools/
    │   └── UnzipShim.cs              # Windows-compatible unzip interface for inspection script
    ├── assets/
    │   ├── hero-agent-team.png
    │   ├── digital-workforce-growth.png
    │   ├── opc-command-center.png
    │   ├── starbay-agent-team.png
    │   ├── agent-project-pipeline.png
    │   ├── ai-builder-camp-workshop.png
    │   ├── starbay-home.png
    │   ├── course-page-hero.png
    │   └── registration-qr.png
    ├── template-inspect/
    ├── template-starter-preview/
    ├── template-starter-layout/
    └── rendered/
        ├── final/
        └── final-montage.png
```

---

### Task 1: Create the build contract and validate the approved content

**Files:**
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/content.json`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/validate-content.mjs`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/source-notes.txt`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/qa-ledger.txt`
- Read: `Course1/HarnessEngineeringPPT/courseVedio/docs/superpowers/specs/2026-08-12-starbay-six-month-ai-agent-transformation-roadshow-design.md`

**Interfaces:**
- Produces: `content.json` with `{ deckTitle, slides[] }`.
- Each slide object contains `{ number, sourceSlide, title, eyebrow, body[], callout, timingSeconds, asset, assetKind, notes[], sources[] }`.
- `validate-content.mjs` exits `0` only when all global content requirements pass.

- [ ] **Step 1: Create the project and build directories**

Run:

```powershell
$project = '.\AIBuilderCampHKCCF'
New-Item -ItemType Directory -Force -Path $project, "$project\build", "$project\build\assets", "$project\build\lib", "$project\build\slides", "$project\build\tools", "$project\build\rendered\final" | Out-Null
```

Expected: all directories in the file structure exist; the source roadshow directory remains untouched.

- [ ] **Step 2: Record the source deck hash and authoritative sources**

Write `source-notes.txt` with the source PPTX SHA-256 plus these sources:

```text
https://starbaymedia.com/
https://starbaymedia.com/activity/ai-weekend-enterprise-bootcamp/
https://empowerwithai.camp/abce
https://www.hkccf-expo.com/
https://www.hkccf-expo.com/ai-dtz
https://www.hkccf-expo.com/aidtzforum2026
https://www.cnbc.com/2026/03/20/nvidia-ai-agents-tokens-human-workers-engineer-jobs-unemployment-jensen-huang.html
https://www.reuters.com/world/india/indias-tcs-chairman-expects-ai-agents-equal-employee-count-2026-06-09/
https://www.goldmansachs.com/insights/articles/what-to-expect-from-ai-in-2026-personal-agents-mega-alliances
```

Run:

```powershell
Get-FileHash -Algorithm SHA256 '.\AIBuilderCampRoadshow\AI_Builder_Camp_15min_Roadshow_2026-08-29_30.pptx'
```

Expected: one SHA-256 value copied into `source-notes.txt` as `source_deck_sha256_before=`.

- [ ] **Step 3: Create `content.json` from the approved 13-slide contract**

Use the full visible copy and Cantonese notes from the approved design spec. Lock this slide table in `content.json`:

| # | Source | Exact title | Primary content | Asset | Sources required |
|---|---:|---|---|---|---|
| 1 | 1 | 未來，你唔係一個人工作／你會帶住一隊 AI Agent | 灣星半年 AI Native 轉型實戰｜由服務客戶到培養 AI Agent Boss | `hero-agent-team.png` | HKCCF official site |
| 2 | 5 | 未來，數碼員工可能比人類員工更多 | 產業預測，不是現況統計；人類編排專門 Agent | `digital-workforce-growth.png` | CNBC, Reuters, Goldman Sachs |
| 3 | 8 | OPC 唔係一個人做晒，而係一個人帶一支 AI 團隊 | 研究、內容、設計／開發、檢查、項目管理 | `opc-command-center.png` | none |
| 4 | 4 | 灣星用半年，開始轉型成 AI Native 公司 | Three approved AI Native principles verbatim | none | Starbay official site |
| 5 | 4 | 四類業務，開始深度融合 AI Agent | 網站建設、視覺設計、活動承辦、AI 實訓 | none | Starbay official site |
| 6 | 8 | 灣星點樣用一支 AI 團隊服務客戶 | 人類項目負責人＋研究／內容／設計開發／檢查／項目 Agent | `starbay-agent-team.png` | user-confirmed Starbay practice |
| 7 | 5 | 一個客戶項目，唔再由一個人由頭做到尾 | 需要→研究→方案→交付物→檢查→交付→知識沉澱 | `agent-project-pipeline.png` | user-confirmed Starbay practice |
| 8 | 6 | 灣星唔想永遠代你執行，而係幫你建立自己嘅 Agent Team | AI 場景實訓→諮詢指導→項目陪跑 | none | user-confirmed Starbay positioning |
| 9 | 2 | 第一步唔係買工具，而係揀啱一個真實場景 | 重複出現、輸入成果清楚、可由人驗收 | none | course page |
| 10 | 6 | 灣星正在建立不同階段嘅 AI 實訓入口 | 企業主、中學生、大學生、在職與企業；合作邀請 | none | course page plus user-confirmed programmes |
| 11 | 5 | 灣星連接港科大（廣州）科研場景開展 AI 實訓 | Include the required visit boundary sentence | `course-page-hero.png` | Starbay activity page and course page |
| 12 | 8 | 8 月 29–30 日：企業主由 AI User 進化成 AI Agent Boss | Day 1 prototype; Day 2 Skill, Agent Team and 90-day route | `ai-builder-camp-workshop.png` | course page |
| 13 | 10 | 帶一項真實業務嚟，帶一支 AI 團隊返去 | Date, Nansha, fee, registration QR, secondary partnership CTA | `registration-qr.png` | course page |

Use timings `[45,55,60,70,55,70,65,60,55,65,55,70,50]`, totalling 775 seconds.

- [ ] **Step 4: Create a deterministic content validator**

Implement `validate-content.mjs` with these checks:

```js
import assert from "node:assert/strict";
import fs from "node:fs";

const data = JSON.parse(fs.readFileSync(new URL("./content.json", import.meta.url), "utf8"));
assert.equal(data.slides.length, 13, "deck must contain 13 slides");
assert.deepEqual(data.slides.map((s) => s.number), Array.from({ length: 13 }, (_, i) => i + 1));
assert.equal(data.slides.reduce((sum, s) => sum + s.timingSeconds, 0), 775);

const visible = data.slides.map((s) => [s.title, s.eyebrow, ...(s.body ?? []), s.callout].filter(Boolean).join("\n")).join("\n");
for (const required of [
  "半年",
  "網站建設",
  "視覺設計",
  "活動承辦",
  "AI 實訓",
  "灣星連接港科大（廣州）科研場景開展 AI 實訓",
  "掃碼報名 AI Builder Camp",
]) assert.ok(visible.includes(required), `missing required copy: ${required}`);

for (const forbidden of ["兩個月", "两个月", "聯合主辦", "校方課程", "教授授課", "官方認證", "港科大背書"])
  assert.ok(!visible.includes(forbidden), `forbidden visible claim: ${forbidden}`);

const generated = new Set(data.slides.filter((s) => s.assetKind === "generated").map((s) => s.asset));
assert.ok(generated.size >= 6, "at least six different ImageGen assets are required");
for (const n of [2, 4, 11, 12, 13]) assert.ok(data.slides[n - 1].sources.length > 0, `slide ${n} requires sources`);

console.log("content contract passed");
```

- [ ] **Step 5: Run the contract check and record the checkpoint**

Run:

```powershell
& 'node' '.\AIBuilderCampHKCCF\build\validate-content.mjs'
```

Expected: `content contract passed`.

Append to `qa-ledger.txt`:

```text
Checkpoint 1 — content contract: PASS — 13 slides, 775 seconds, required wording and source coverage verified.
```

---

### Task 2: Inspect the source template and build the 13-slide starter deck

**Files:**
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/tools/UnzipShim.cs`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/template-audit.txt`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/template-frame-map.json`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/edit-plan.json`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/deviation-log.txt`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/template-starter.pptx`

**Interfaces:**
- Consumes: source PPTX and `content.json`.
- Produces: a 13-slide starter whose every slide is a duplicated source slide.
- Produces: `edit-plan.json` mapping semantic roles such as `title`, `body1`, `heroImage`, `footer`, and `pageNumber` to exact inherited IDs.

- [ ] **Step 1: Read the required artifact-tool references**

Read completely before editing the template:

```text
artifact_tool_docs/API_QUICK_START.md
artifact_tool_docs/api/API_DOCS.md
artifact_tool_docs/api/references/master.spec.md
artifact_tool_docs/api/references/layout.spec.md
artifact_tool_docs/api/references/inspect.md
artifact_tool_docs/api/references/cookbook/imported-deck.md
artifact_tool_docs/api/references/images.spec.md
artifact_tool_docs/api/references/speaker-notes.spec.md
```

- [ ] **Step 2: Create a Windows `unzip` compatibility executable for the inspection script**

Use this exact `UnzipShim.cs` implementation:

```csharp
using System;
using System.IO;
using System.IO.Compression;

public static class Program {
  public static int Main(string[] args) {
    if (args.Length == 2 && args[0] == "-Z1") {
      using (var archive = ZipFile.OpenRead(args[1]))
        foreach (var entry in archive.Entries) Console.WriteLine(entry.FullName.Replace('\\', '/'));
      return 0;
    }
    if (args.Length == 3 && args[0] == "-p") {
      using (var archive = ZipFile.OpenRead(args[1])) {
        var wanted = args[2].Replace('\\', '/');
        foreach (var entry in archive.Entries) {
          if (!String.Equals(entry.FullName.Replace('\\', '/'), wanted, StringComparison.Ordinal)) continue;
          using (var input = entry.Open()) using (var output = Console.OpenStandardOutput()) input.CopyTo(output);
          return 0;
        }
      }
      Console.Error.WriteLine("entry not found: " + args[2]);
      return 2;
    }
    Console.Error.WriteLine("usage: unzip -Z1 archive | unzip -p archive entry");
    return 2;
  }
}
```

Compile it to `build/tools/unzip.exe`, reference `System.IO.Compression.FileSystem`, and prepend `build/tools` to the process `PATH`:

```powershell
$build = '.\AIBuilderCampHKCCF\build'
$sourcePptx = '.\AIBuilderCampRoadshow\AI_Builder_Camp_15min_Roadshow_2026-08-29_30.pptx'
$cs = Get-Content -LiteralPath "$build\tools\UnzipShim.cs" -Raw -Encoding UTF8
Add-Type -TypeDefinition $cs -ReferencedAssemblies 'System.IO.Compression.dll','System.IO.Compression.FileSystem.dll' -OutputAssembly "$build\tools\unzip.exe" -OutputType ConsoleApplication
$env:PATH = "$build\tools;$env:PATH"
& "$build\tools\unzip.exe" -Z1 $sourcePptx
& "$build\tools\unzip.exe" -p $sourcePptx 'ppt/presentation.xml'
```

Expected: the first command lists package entries; the second emits presentation XML.

- [ ] **Step 3: Initialize artifact-tool and inspect every source slide**

Run the bundled workspace setup and `inspect_template_deck.mjs`:

```powershell
$node = 'node'
$skill = '.\skills\presentations'
$build = '.\AIBuilderCampHKCCF\build'
$sourcePptx = '.\AIBuilderCampRoadshow\AI_Builder_Camp_15min_Roadshow_2026-08-29_30.pptx'
$env:PATH = "$build\tools;$env:PATH"
& $node "$skill\container_tools\setup_artifact_tool_workspace.mjs" --workspace $build
& $node "$skill\template_following_scripts\inspect_template_deck.mjs" --workspace $build --pptx $sourcePptx
```

Expected: 10 source PNGs, 10 layout JSON files, `template-inspect.ndjson`, extracted media, font evidence, and `template-manifest.json` under `build/template-inspect/`.

- [ ] **Step 4: Inspect all 10 source slides and write the template audit**

Record these verified layout roles in `template-audit.txt`:

```text
Source 1 — dark cover with left title and right hero image
Source 2 — dark four-row evidence/list page
Source 4 — dark numbered four-row result page
Source 5 — dark left copy and right large image
Source 6 — light two-column comparison/schedule page
Source 8 — dark left copy and right large image with compact rows
Source 10 — dark CTA page with large QR block
```

Also record exact font family, font sizes, page chrome IDs, image IDs, inherited placeholders, margins, title bounds, and any master/layout objects. Compare every render to the existing source montage rather than sampling representative slides.

- [ ] **Step 5: Create the exact output-to-source map**

Use this mapping in `template-frame-map.json`:

```json
{
  "outputSlides": [
    { "outputSlide": 1, "sourceSlide": 1, "narrativeRole": "opening thesis", "reuseMode": "duplicate-slide" },
    { "outputSlide": 2, "sourceSlide": 5, "narrativeRole": "future trend", "reuseMode": "duplicate-slide" },
    { "outputSlide": 3, "sourceSlide": 8, "narrativeRole": "OPC definition", "reuseMode": "duplicate-slide" },
    { "outputSlide": 4, "sourceSlide": 4, "narrativeRole": "AI Native principles", "reuseMode": "duplicate-slide" },
    { "outputSlide": 5, "sourceSlide": 4, "narrativeRole": "four businesses", "reuseMode": "duplicate-slide" },
    { "outputSlide": 6, "sourceSlide": 8, "narrativeRole": "Starbay Agent Team", "reuseMode": "duplicate-slide" },
    { "outputSlide": 7, "sourceSlide": 5, "narrativeRole": "project pipeline", "reuseMode": "duplicate-slide" },
    { "outputSlide": 8, "sourceSlide": 6, "narrativeRole": "service model shift", "reuseMode": "duplicate-slide" },
    { "outputSlide": 9, "sourceSlide": 2, "narrativeRole": "scene selection", "reuseMode": "duplicate-slide" },
    { "outputSlide": 10, "sourceSlide": 6, "narrativeRole": "training entry points", "reuseMode": "duplicate-slide" },
    { "outputSlide": 11, "sourceSlide": 5, "narrativeRole": "HKUST GZ research scene", "reuseMode": "duplicate-slide" },
    { "outputSlide": 12, "sourceSlide": 8, "narrativeRole": "two-day camp outcomes", "reuseMode": "duplicate-slide" },
    { "outputSlide": 13, "sourceSlide": 10, "narrativeRole": "registration CTA", "reuseMode": "duplicate-slide" }
  ],
  "omittedSourceSlides": [
    { "sourceSlide": 3, "reason": "five-step white process page is not needed" },
    { "sourceSlide": 7, "reason": "three-part schedule has no image slot for the approved pipeline visual" },
    { "sourceSlide": 9, "reason": "eight-item asset inventory is denser than the approved narrative" }
  ]
}
```

For each output slide, add `editTargets` using exact `shapeId`, `sourceElementId`, or image ID values from `template-inspect.ndjson`. Classify every inherited object as `keep`, `rewrite`, `replace`, or `delete`; do not use unbounded overlay additions.

- [ ] **Step 6: Create `edit-plan.json` and the intentional deviation log**

`edit-plan.json` must expose stable semantic roles per output slide. Slide 1 requires `title`, `subtitle`, `eyebrow`, `date`, `heroImage`, `footer`, and `pageNumber`; slides 2, 3, 6, 7, 11, and 12 require `title`, all inherited body-row roles, `callout`, `heroImage`, `footer`, and `pageNumber`; slides 4, 5, and 9 require `title`, four numbered-row roles, their separators, `callout`, `footer`, and `pageNumber`; slides 8 and 10 require `title`, both column-heading roles, both column-body roles, `callout`, `footer`, and `pageNumber`; slide 13 requires `title`, date, location, fee, qualification line, primary CTA, secondary CTA, QR image, footer, and page number. Every role value must be an actual inherited ID copied from `template-inspect.ndjson`.

Log one global typography deviation: use Noto Sans TC if installed, otherwise Microsoft JhengHei, while preserving source font sizes, weights, line spacing, insets, alignment, and anchors. Log slide 4's deletion of the unused fourth row and any QR/image replacement.

- [ ] **Step 7: Build and validate the starter deck**

Run `prepare_template_starter_deck.mjs` using the source PPTX and frame map:

```powershell
$node = 'node'
$skill = '.\skills\presentations'
$build = '.\AIBuilderCampHKCCF\build'
$sourcePptx = '.\AIBuilderCampRoadshow\AI_Builder_Camp_15min_Roadshow_2026-08-29_30.pptx'
& $node "$skill\template_following_scripts\prepare_template_starter_deck.mjs" --workspace $build --pptx $sourcePptx --map "$build\template-frame-map.json" --out "$build\template-starter.pptx" --preview-dir "$build\template-starter-preview" --layout-dir "$build\template-starter-layout" --contact-sheet "$build\template-starter-contact-sheet.png"
```

Expected:

```text
template-starter.pptx contains 13 slides
every slide is duplicated from its mapped source
template-frame-map validation passes
template-starter-preview contains 13 PNGs
template-starter-layout contains 13 layout JSON files
```

Append to `qa-ledger.txt`:

```text
Checkpoint 2 — template starter: PASS — 13 mapped duplicate slides; inherited element IDs and placeholders classified.
```

---

### Task 3: Produce and verify the real and generated visual assets

**Files:**
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/image-prompts.txt`
- Create: six generated PNG files under `build/assets/`
- Copy: three authentic assets under `build/assets/`

**Interfaces:**
- Consumes: exact image slots measured from starter-slide layout JSON.
- Produces: six unique, slide-ready ImageGen assets plus authentic Starbay/course/QR assets.

- [ ] **Step 1: Copy authentic assets into the new project**

Copy without modifying the originals:

```text
.\assets\reference-screenshot.png
  → build/assets/starbay-home.png

Course1/HarnessEngineeringPPT/AIBuilderCampRoadshow/build/assets/website-hero.png
  → build/assets/course-page-hero.png

Course1/HarnessEngineeringPPT/AIBuilderCampRoadshow/build/assets/alvin-course-consultation-qr.png
  → build/assets/registration-qr.png
```

Open each copied image and verify that the first is Starbay's home page, the second is the official course-page hero, and the third is the existing registration/consultation QR.

- [ ] **Step 2: Generate the six Image 2 assets with the built-in ImageGen tool**

Use one built-in call per asset. Each final prompt must preserve the following exact composition intent:

```text
hero-agent-team.png
Use case: ads-marketing. Asset type: 16:9 PowerPoint cover hero. A confident Asian enterprise project leader stands on the right side of a refined near-future workspace overlooking a Greater Bay Area night skyline; behind and around the person, six abstract luminous AI agent presences form a coordinated team through elegant blue task trails and nodes. Premium enterprise technology photography, deep navy, electric blue, cold white, restrained gold, cinematic but credible, generous dark negative space on the left for a two-line title. Concept visual, not documentary photography. No text, no logo, no watermark, no robot faces, no readable UI, no fake statistics.

digital-workforce-growth.png
Use case: stylized-concept. Asset type: right-side image for a 16:9 business presentation. One Asian human coordinator in the foreground, with an expanding field of abstract digital agent nodes and task trails receding into the distance, suggesting a fast-growing digital workforce without showing numbers. Deep navy and electric blue, editorial corporate realism, high contrast, subject kept to the right half, clean crop. Concept visual. No text, logo, watermark, robots, charts, percentages, or readable UI.

opc-command-center.png
Use case: ads-marketing. Asset type: right-side image for an OPC presentation slide. One Asian entrepreneur calmly leads five specialized abstract AI agent presences representing research, content, design-development, quality review, and project management; elegant command-center composition with the human visibly making decisions while agents execute. Dark navy, electric blue and subtle gold, premium credible enterprise photography, room for slide copy on the left. No embedded labels, text, logo, watermark, humanoid robots, or readable screens.

starbay-agent-team.png
Use case: stylized-concept. Asset type: right-side visual for a corporate presentation. A human project lead at the centre-right coordinates a polished network of five specialized AI agents; visual cues suggest research documents, content, design-development, quality checking, and project orchestration without readable interfaces. Greater Bay Area professional atmosphere, deep navy, electric blue, cold white, restrained gold, premium enterprise realism. No text, logo, watermark, fake client brands, or robot faces.

agent-project-pipeline.png
Use case: productivity-visual. Asset type: right-side visual for a project workflow slide. A human project owner oversees a clean horizontal digital production pipeline moving from client need and research through solution creation, website-visual-event deliverables, review, delivery, and knowledge capture; represent stages through abstract illuminated work objects and connected task trails, not labels. Deep navy corporate technology aesthetic, electric blue with restrained gold, high legibility at presentation size. No text, logos, watermark, fake UI, or statistics.

ai-builder-camp-workshop.png
Use case: ads-marketing. Asset type: right-side image for a training presentation. A diverse group of adult Asian entrepreneurs work together on laptops in a credible future-facing AI workshop; one facilitator helps them orchestrate abstract AI agent task trails. Premium modern learning space, energetic but realistic, deep navy and electric blue with warm human skin tones, no visible university branding. Concept visual, not a real event photo. No text, logo, watermark, school emblem, fake readable screens, or robot faces.
```

- [ ] **Step 3: Inspect every output and perform targeted iterations**

For each image, verify subject placement against its measured template slot, facial and hand integrity, lack of readable fake UI, absence of logos/text, and consistent palette. If an image fails, make one targeted change and regenerate only that asset. Do not accept a visually attractive image whose subject is cropped by the inherited frame.

- [ ] **Step 4: Save final images and prompt provenance**

Copy selected outputs from ImageGen's default location into `build/assets/`. For every asset, record its actual filename, `tool_mode=built-in ImageGen`, the complete final prompt, `inspection_result=PASS`, and the exact iteration note or `iteration_note=none` in `image-prompts.txt`.

No project-referenced image may remain only under the default generated-images directory.

- [ ] **Step 5: Record the asset checkpoint**

Append to `qa-ledger.txt`:

```text
Checkpoint 3 — visual assets: PASS — six unique generated images and three authentic assets inspected, saved and sourced.
```

---

### Task 4: Implement the deck editing helpers and slides 1–5

**Files:**
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/lib/deck-helpers.mjs`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/preview-batch.mjs`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/slides/slides-01-05.mjs`

**Interfaces:**
- `createDeckContext({ presentation, content, editPlan, assetDir, outputDir })` returns a context object.
- `setText(ctx, slideNumber, role, text)` replaces the complete inherited text frame.
- `replaceImage(ctx, slideNumber, role, assetName, alt)` replaces an inherited image with byte-backed PNG data.
- `deleteTarget(ctx, slideNumber, role)` removes only an element classified `delete` in the frame map.
- `setSpeakerNotes(ctx, slideNumber)` writes the Cantonese notes and `[Sources]` block from `content.json`.
- `renderSlides(ctx, slideNumbers, outputDir)` exports full-size PNG and layout JSON evidence.
- `exportMontage(ctx, outputPath)` writes the complete deck montage.
- `exportInspection(ctx, outputPath)` writes slide, textbox, shape, image, notes, and layout inspection NDJSON.
- `applySlides01To05(ctx)` edits slides 1–5 only.

- [ ] **Step 1: Implement strict inherited-element helpers**

Use artifact-tool import and exact IDs:

```js
function targetFor(ctx, slideNumber, role) {
  const id = ctx.editPlan.slides[String(slideNumber)]?.[role];
  if (!id) throw new Error(`missing inherited target: slide ${slideNumber} role ${role}`);
  const target = ctx.presentation.resolve(id);
  if (!target) throw new Error(`unresolved inherited target: ${id}`);
  return target;
}

export function setText(ctx, slideNumber, role, value) {
  targetFor(ctx, slideNumber, role).textFrame.setText(value);
}

export function setSpeakerNotes(ctx, slideNumber) {
  const slide = ctx.presentation.slides.items[slideNumber - 1];
  const item = ctx.content.slides[slideNumber - 1];
  const sourceBlock = item.sources.length ? `\n\n[Sources]\n${item.sources.join("\n")}` : "";
  slide.speakerNotes.textFrame.setText(`${item.notes.join("\n\n")}${sourceBlock}`);
  slide.speakerNotes.setVisible(true);
}
```

`replaceImage` must call the inherited image object's `replace()` method with local bytes; do not add a second image over the original.

- [ ] **Step 2: Implement slides 1–5 using inherited roles**

Apply these edits:

```text
Slide 1: replace title/subtitle/eyebrow/date; replace hero with hero-agent-team.png.
Slide 2: replace title, forecast qualifier and short explanation; replace image with digital-workforce-growth.png.
Slide 3: replace title and five role rows; replace image with opc-command-center.png.
Slide 4: replace title and first three numbered rows with the approved principles; delete the inherited fourth row and its number/line as classified.
Slide 5: replace title and four numbered rows with the four businesses and outcome words.
```

Preserve inherited margins, page chrome, font sizes, weights, line spacing, paragraph spacing, insets, alignment, and vertical anchors. Shorten supporting copy before changing type size.

- [ ] **Step 3: Write speaker notes for slides 1–5**

Each note must include the approved timing, a natural Cantonese talk track, a transition to the next slide, a factual boundary, and sources where required. Slide 2 must explicitly say that the figures are industry forecasts; slide 4 must avoid unsupported performance metrics.

- [ ] **Step 4: Render and inspect the first batch**

Run:

```powershell
& 'node' '.\AIBuilderCampHKCCF\build\preview-batch.mjs' --module 'slides/slides-01-05.mjs' --slides '1-5'
```

Expected: five PNGs and five layout JSON files. Inspect each PNG at full size and record title wrapping, image crop, hierarchy, and retained chrome in `qa-ledger.txt`.

- [ ] **Step 5: Record the checkpoint**

Append:

```text
Checkpoint 4 — slides 1–5: PASS — opening, trend, OPC, principles and four-business narrative visually verified.
```

---

### Task 5: Implement slides 6–10

**Files:**
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/slides/slides-06-10.mjs`

**Interfaces:**
- Consumes: the same context and inherited-target helper API from Task 4.
- Produces: `applySlides06To10(ctx)`.

- [ ] **Step 1: Implement slides 6–10**

Apply these edits:

```text
Slide 6: human project lead plus five Agent roles; replace right image with starbay-agent-team.png; keep human responsibilities visible.
Slide 7: group the seven-step flow into four inherited copy rows; replace right image with agent-project-pipeline.png; keep the exact full flow in notes.
Slide 8: use the inherited two-column structure for 「過去：代替執行」 versus 「現在：實訓／諮詢／陪跑」; end with the approved Starbay Agent Team statement.
Slide 9: use three inherited numbered rows for the real-scene questions; use the fourth row/callout for business examples and the human-verification rule.
Slide 10: use the inherited two-column structure for enterprise owners/current workers and secondary/university students; place the school, youth and enterprise partnership invitation in the bottom callout.
```

- [ ] **Step 2: Write speaker notes for slides 6–10**

Make the human role explicit on slides 6–9: commercial judgement, creative direction, relationships, and final acceptance remain human responsibilities. Slide 10 must state that 29–30 August primarily serves enterprise owners, winter serves secondary students, and university projects are conducted with two-region youth associations.

- [ ] **Step 3: Render and inspect the second batch**

Run:

```powershell
& 'node' '.\AIBuilderCampHKCCF\build\preview-batch.mjs' --module 'slides/slides-06-10.mjs' --slides '6-10'
```

Expected: five PNGs and five layout JSON files. Inspect slides 6, 7, and 8 consecutively to ensure their silhouettes differ despite sharing dark navy styling.

- [ ] **Step 4: Record the checkpoint**

Append:

```text
Checkpoint 5 — slides 6–10: PASS — Agent service model, project flow, new positioning, scene selection and training entries verified.
```

---

### Task 6: Implement slides 11–13, compose the deck, and export PPTX

**Files:**
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/slides/slides-11-13.mjs`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/deck.mjs`
- Create: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/Starbay_AI_Agent_Boss_HKCCF_15min_2026-08-29-30.pptx`

**Interfaces:**
- Produces: `applySlides11To13(ctx)`.
- `deck.mjs` imports `template-starter.pptx`, calls all three slide modules, sets notes on all slides, exports per-slide PNG/layout evidence, montage, inspect NDJSON, and final PPTX.

- [ ] **Step 1: Implement slides 11–13**

Apply these edits:

```text
Slide 11: exact HKUST(GZ) connection sentence; replace right image with course-page-hero.png; include the activity-arrangement boundary in visible small copy.
Slide 12: Day 1 and Day 2 outcome blocks; replace right image with ai-builder-camp-workshop.png; identify the image as a concept visual in a discreet caption or notes according to the approved layout.
Slide 13: date, Nansha location, fees, qualification condition, main registration CTA and secondary cooperation line; replace the inherited QR image with registration-qr.png; keep the QR on a plain high-contrast field.
```

- [ ] **Step 2: Implement `deck.mjs` as the single composition/export entry point**

Use this flow:

```js
const presentation = await PresentationFile.importPptx(await FileBlob.load(STARTER_PPTX));
const ctx = createDeckContext({ presentation, content, editPlan, assetDir: ASSET_DIR, outputDir: FINAL_RENDER_DIR });
await applySlides01To05(ctx);
await applySlides06To10(ctx);
await applySlides11To13(ctx);
for (let n = 1; n <= 13; n += 1) setSpeakerNotes(ctx, n);
await renderSlides(ctx, Array.from({ length: 13 }, (_, i) => i + 1), FINAL_RENDER_DIR);
await exportMontage(ctx, FINAL_MONTAGE);
await exportInspection(ctx, FINAL_INSPECT);
const pptx = await PresentationFile.exportPptx(presentation);
await pptx.save(FINAL_PPTX);
```

Use absolute paths resolved from `import.meta.url`. Fail immediately if the imported starter does not contain 13 slides or any mapped element ID cannot be resolved.

- [ ] **Step 3: Run the complete content and deck build**

Run the content validator, then `deck.mjs`:

```powershell
$node = 'node'
$build = '.\AIBuilderCampHKCCF\build'
& $node "$build\validate-content.mjs"
& $node "$build\deck.mjs"
```

Expected:

```text
content contract passed
13 final PNGs
13 final layout JSON files
one final montage
one final inspect NDJSON
one final PPTX
```

- [ ] **Step 4: Verify the QR asset before visual QA**

Open `registration-qr.png` at original resolution and scan it with an independent QR reader if available. Confirm it resolves to the intended consultation/registration route. If it cannot be decoded, regenerate a plain black-on-white QR from `https://empowerwithai.camp/abce`, replace the asset, and record the change in `source-notes.txt`.

- [ ] **Step 5: Record the checkpoint**

Append:

```text
Checkpoint 6 — full export: PASS — 13-slide PPTX, renders, layout evidence, notes and QR generated.
```

---

### Task 7: Run template fidelity, overflow, source, and full-size visual QA

**Files:**
- Modify: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/build/qa-ledger.txt`
- Modify as needed: slide modules, `content.json`, `edit-plan.json`, frame map, or assets
- Verify: final PPTX and all final render evidence

**Interfaces:**
- Consumes: final PPTX, starter PPTX, frame map, final layouts and renders.
- Produces: a clean final deck and a complete QA ledger with one line per slide.

- [ ] **Step 1: Run structural and overflow checks**

Run:

```powershell
$python = 'python'
$node = 'node'
$skill = '.\skills\presentations'
$build = '.\AIBuilderCampHKCCF\build'
$final = '.\AIBuilderCampHKCCF\Starbay_AI_Agent_Boss_HKCCF_15min_2026-08-29-30.pptx'
& $python "$skill\container_tools\slides_test.py" $final
& $node "$skill\template_following_scripts\check_template_fidelity.mjs" --workspace $build --starter-pptx "$build\template-starter.pptx" --final-pptx $final --map "$build\template-frame-map.json" --starter-layout-dir "$build\template-starter-layout" --final-layout-dir "$build\rendered\final" --edit-dir $build
```

Expected: no slide-canvas overflow, no unintended additions/deletions, and no unhandled inherited placeholders.

- [ ] **Step 2: Inspect all 13 slides individually at full size**

For every slide, record in `qa-ledger.txt`:

For each slide number from 1 through 13, write a completed line containing `primary read`, `title fit`, `image crop`, `spacing`, `source/claim`, and `notes`, each marked `PASS` or `FAIL`, followed by either `fix applied: none` or the exact correction made.

Check all generated faces/hands/screens at full-slide size. Replace any asset that is distorted, poorly framed, blurry, off-palette, or visually inconsistent.

- [ ] **Step 3: Inspect the montage for narrative rhythm**

Verify that adjacent silhouettes vary, dark/light pacing is coherent, the first three slides build future tension, slides 4–8 prove the Starbay transformation, and slides 11–13 visibly accelerate toward registration. The montage is not a substitute for the per-slide inspection.

- [ ] **Step 4: Verify visible copy, notes, and sources from the final inspection output**

Search final inspect NDJSON for:

```text
半年
網站建設
視覺設計
活動承辦
AI 實訓
灣星連接港科大（廣州）科研場景開展 AI 實訓
掃碼報名 AI Builder Camp
[Sources]
```

Confirm the old transformation-period wording and unsupported cooperation claims are absent from visible text. Confirm every externally sourced non-trivial claim and external asset is traced in that slide's notes.

- [ ] **Step 5: Rebuild after every correction and rerun all checks**

Do not patch the exported PPTX. Correct the source content, inherited-element edit, frame map, or image asset; rerun `deck.mjs`, overflow tests, fidelity tests, and affected full-size slide inspections.

- [ ] **Step 6: Record the final QA checkpoint**

Append:

```text
Checkpoint 7 — final QA: PASS — all 13 slides inspected full size; overflow, template fidelity, wording, sources, notes and visual consistency verified.
```

---

### Task 8: Verify preservation and hand off the final deck

**Files:**
- Verify: source deck unchanged
- Deliver: `Course1/HarnessEngineeringPPT/AIBuilderCampHKCCF/Starbay_AI_Agent_Boss_HKCCF_15min_2026-08-29-30.pptx`

**Interfaces:**
- Produces: one user-facing final PPTX citation and a concise summary.

- [ ] **Step 1: Recompute the source-deck hash**

Run `Get-FileHash -Algorithm SHA256` on the original PPTX and compare it with `source_deck_sha256_before` in `source-notes.txt`.

Expected: hashes match exactly. Append `source_deck_preserved=PASS`.

- [ ] **Step 2: Verify the final output exists and is non-empty**

Run `Get-Item` on the final PPTX and confirm it opens through the final render/export checks. Do not deliver the starter PPTX, build files, prompt ledger, or QA images unless the user asks.

- [ ] **Step 3: Hand off the completed deck**

Return a short summary covering the 13-slide HKCCF narrative, six Image 2 visuals, Cantonese notes, AI Builder Camp CTA, and source/claim safeguards. Cite the final deck exactly once as the output artifact.

Append:

```text
Checkpoint 8 — delivery: PASS — source preserved and final PPTX handed off.
```
