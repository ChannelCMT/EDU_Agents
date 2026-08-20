import fs from 'node:fs/promises';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const OUT = new URL('.', import.meta.url).pathname.replace(/^\/(?:C:)/, 'C:').replaceAll('/', '\\');
const QA = `${OUT}..\\qa\\ppt`;
await fs.mkdir(QA, { recursive: true });

const C = {
  bg: '#06182A',
  panel: '#0A2F4E',
  panel2: '#0C2B49',
  white: '#F7FBFF',
  blue: '#8ED6FF',
  gray: '#B8C4D2',
  yellow: '#FFD66F',
  green: '#A0E6BF',
  red: '#FFB1B1',
  line: '#2B638A',
};

async function writeBlob(path, blob) {
  return fs.writeFile(path, new Uint8Array(await blob.arrayBuffer()));
}

function box(slide, geometry, position, fill = 'none', lineFill = 'none', lineWidth = 0, name) {
  return slide.shapes.add({
    geometry,
    name,
    position,
    fill,
    line: { style: 'solid', fill: lineFill, width: lineWidth },
    borderRadius: geometry === 'roundRect' ? 20 : undefined,
  });
}

function text(slide, value, position, style = {}, name) {
  const s = box(slide, 'textbox', position, 'none', 'none', 0, name);
  s.text = value;
  s.text.style = {
    fontSize: style.fontSize ?? 24,
    color: style.color ?? C.white,
    bold: style.bold ?? false,
    alignment: style.alignment ?? 'left',
    verticalAlignment: style.verticalAlignment ?? 'middle',
    wrap: style.wrap ?? 'square',
    lineSpacing: style.lineSpacing ?? 1.12,
  };
  return s;
}

function panel(slide, title, copy, position, accent = C.blue, opts = {}) {
  const p = box(slide, 'roundRect', position, opts.fill ?? C.panel, accent, 2, opts.name);
  text(slide, title, { left: position.left + 28, top: position.top + 22, width: position.width - 56, height: 42 }, { fontSize: opts.titleSize ?? 28, color: opts.titleColor ?? C.white, bold: true }, `${opts.name ?? 'panel'}-title`);
  if (copy) text(slide, copy, { left: position.left + 28, top: position.top + 70, width: position.width - 56, height: position.height - 88 }, { fontSize: opts.bodySize ?? 21, color: opts.bodyColor ?? C.gray, lineSpacing: 1.18 }, `${opts.name ?? 'panel'}-copy`);
  return p;
}

function arrow(slide, x, y, width, label = '→', color = C.blue) {
  text(slide, label, { left: x, top: y - 19, width, height: 42 }, { fontSize: 34, color, bold: true, alignment: 'center' });
}

function addFrame(slide, index, title, label = 'MCP / API / SDK / CLI / ADK') {
  slide.background.fill = C.bg;
  // Match the video master: a restrained top-left and bottom-right blue glow.
  box(slide, 'ellipse', { left: -220, top: -280, width: 720, height: 720 }, 'radial(#2D7CC4/30 0%, #2D7CC4/0 72%)', 'none', 0, `glow-top-left-${index}`);
  box(slide, 'ellipse', { left: 1460, top: 760, width: 680, height: 680 }, 'radial(#2C65A2/24 0%, #2C65A2/0 74%)', 'none', 0, `glow-bottom-right-${index}`);
  // Background grid is intentionally subtle; it must not compete with content.
  // Harness: grid lines are environmental texture only. Keep them near the background value.
  for (let x = 0; x <= 1920; x += 160) box(slide, 'line', { left: x, top: 0, width: 0, height: 1080 }, 'none', '#0B2236', 1);
  for (let y = 0; y <= 1080; y += 160) box(slide, 'line', { left: 0, top: y, width: 1920, height: 0 }, 'none', '#0B2236', 1);
  text(slide, 'AGENT ARCHITECTURE / COURSE LOOP', { left: 76, top: 34, width: 700, height: 34 }, { fontSize: 18, color: C.blue, bold: true }, `eyebrow-${index}`);
  text(slide, label, { left: 1340, top: 34, width: 500, height: 34 }, { fontSize: 18, color: C.yellow, bold: true, alignment: 'right' }, `label-${index}`);
  box(slide, 'line', { left: 76, top: 92, width: 1768, height: 0 }, 'none', '#1B4058', 1);
  text(slide, title, { left: 92, top: 124, width: 1600, height: 86 }, { fontSize: 46, color: C.white, bold: true }, `title-${index}`);
  // Subtitle safe band: no key visual may enter the bottom 180 px.
  box(slide, 'rect', { left: 0, top: 900, width: 1920, height: 180 }, '#03101D', 'none', 0, `subtitle-safe-band-${index}`);
  box(slide, 'line', { left: 76, top: 900, width: 1768, height: 0 }, 'none', '#204B6A', 1);
  text(slide, `字幕安全区（暂不显示）`, { left: 1500, top: 930, width: 310, height: 26 }, { fontSize: 14, color: '#52718A', alignment: 'right' }, `safe-note-${index}`);
}

function addNotes(slide, body) {
  slide.speakerNotes.textFrame.setText([
    body,
    '',
    '[Sources]',
    '- 用户提供的 pasted-text.txt（概念定义、示例与技术关系）',
    '- 本页为审核稿：时间点与动画顺序写在 storyboard/semantic-beat-manifest.yaml。',
  ]);
  slide.speakerNotes.setVisible(true);
}

const deck = Presentation.create({ slideSize: { width: 1920, height: 1080 } });

// 01 Hook
{
  const s = deck.slides.add(); addFrame(s, 1, '这 7 个词，为什么总被混在一起？', 'OPENING / 00:00');
  text(s, '它们看起来都和“调用工具”有关，\n但其实根本不在同一层。', { left: 112, top: 300, width: 900, height: 180 }, { fontSize: 38, color: C.gray, bold: true });
  const terms = [['API', 1180, 300, C.blue], ['SDK', 1380, 420, C.white], ['CLI', 1600, 300, C.yellow], ['Function Calling', 1120, 560, C.white], ['Tool Calling', 1430, 560, C.yellow], ['MCP', 1600, 680, C.blue], ['ADK', 1260, 720, C.yellow]];
  for (const [t, x, y, color] of terms) { const p = box(s, 'roundRect', { left: x, top: y, width: t.length > 10 ? 300 : 180, height: 68 }, C.panel2, color, 2); text(s, t, { left: x + 12, top: y + 6, width: t.length > 10 ? 276 : 156, height: 54 }, { fontSize: t.length > 10 ? 21 : 28, color, bold: true, alignment: 'center' }); }
  panel(s, '先放回地图，再解释每个词', '', { left: 112, top: 650, width: 870, height: 110 }, C.yellow, { titleColor: C.yellow, titleSize: 29, name: 'hook-conclusion' });
  addNotes(s, '开场先承接受众困惑，不在前 5 秒讲 ReAct 或 Multi-Agent。');
}

// 02 Map
{
  const s = deck.slides.add(); addFrame(s, 2, '先看总地图，再解释每个词', 'MAP / 00:16');
  const rows = [
    ['用户 / Agent 应用', '任务从这里进入', C.yellow],
    ['ADK', '状态 · 工作流 · 编排', C.blue],
    ['LLM + Tool Calling', '模型决定何时使用能力', C.blue],
    ['Function Calling / MCP', '工具机制与标准化连接', C.blue],
    ['API · SDK · CLI · 外部系统', '能力真正落地的地方', C.green],
  ];
  rows.forEach(([a,b,color], i) => { const y = 280 + i*112; box(s, 'roundRect', { left: 250, top: y, width: 1420, height: 78 }, C.panel, color, 2); text(s, a, { left: 285, top: y+10, width: 640, height: 56 }, { fontSize: 29, color: color, bold: true }); text(s, b, { left: 1070, top: y+10, width: 540, height: 56 }, { fontSize: 21, color: C.gray, alignment: 'right' }); });
  text(s, '从上到下：组织 → 决策 → 连接 → 执行', { left: 480, top: 850, width: 960, height: 42 }, { fontSize: 28, color: C.white, bold: true, alignment: 'center' });
  addNotes(s, '总图是全片主视觉，后续每页都从这里局部放大，再回到总图。');
}

// 03 Access layer
{
  const s = deck.slides.add(); addFrame(s, 3, 'API、SDK、CLI：软件怎样使用能力', 'ACCESS LAYER / 00:40');
  panel(s, 'API', '软件之间的\n能力契约', { left: 140, top: 385, width: 430, height: 220 }, C.blue, { titleColor: C.blue, bodySize: 26, name: 'api' });
  arrow(s, 585, 493, 170);
  panel(s, 'SDK', '把认证、重试和\n错误处理封装起来', { left: 745, top: 385, width: 430, height: 220 }, C.yellow, { titleColor: C.yellow, bodySize: 25, name: 'sdk' });
  arrow(s, 1190, 493, 170);
  panel(s, 'CLI', '人、脚本或 Agent\n的终端入口', { left: 1350, top: 385, width: 430, height: 220 }, C.green, { titleColor: C.green, bodySize: 25, name: 'cli' });
  panel(s, '同一个服务的三种入口', 'API 面向程序，SDK 面向开发者，CLI 面向终端操作。', { left: 380, top: 690, width: 1160, height: 115 }, C.blue, { titleSize: 30, bodySize: 22, name: 'access-summary' });
  addNotes(s, '用一个订单接口例子解释 API，再展示 SDK 封装和 CLI 入口。');
}

// 04 Model tool layer
{
  const s = deck.slides.add(); addFrame(s, 4, 'Function Calling 是具体机制，Tool Calling 是总机制', 'MODEL TOOL LAYER / 01:03');
  panel(s, 'LLM', '提出调用请求', { left: 140, top: 380, width: 310, height: 180 }, C.yellow, { titleColor: C.yellow, titleSize: 31, bodySize: 24, name: 'llm' });
  arrow(s, 470, 448, 130);
  panel(s, '结构化请求', 'name: get_weather\ncity: Tokyo', { left: 620, top: 360, width: 430, height: 220 }, C.blue, { titleSize: 29, bodySize: 24, name: 'request' });
  arrow(s, 1080, 448, 130);
  panel(s, 'Executor', '应用程序真正\n执行函数', { left: 1230, top: 380, width: 360, height: 180 }, C.green, { titleColor: C.green, titleSize: 31, bodySize: 24, name: 'executor' });
  panel(s, 'TOOL', 'Function · Web Search · File Search · Computer · MCP', { left: 300, top: 700, width: 1320, height: 115 }, C.yellow, { titleColor: C.yellow, titleSize: 32, bodySize: 21, name: 'tool-umbrella' });
  text(s, 'Function ⊂ Tool', { left: 740, top: 620, width: 420, height: 50 }, { fontSize: 29, color: C.yellow, bold: true, alignment: 'center' });
  addNotes(s, '关键不是“模型自己执行代码”，而是模型输出结构化请求，应用程序负责执行。');
}

// 05 MCP
{
  const s = deck.slides.add(); addFrame(s, 5, 'MCP：把外部能力接得更标准', 'CONNECTION LAYER / 01:28');
  panel(s, '没有 MCP', 'GitHub · Slack · Notion · DB\n每接一个，就写一套适配器\nIntegration Explosion', { left: 110, top: 380, width: 520, height: 265 }, C.red, { titleColor: C.red, titleSize: 31, bodySize: 23, name: 'explosion' });
  arrow(s, 650, 482, 120);
  panel(s, 'MCP Client', '统一发现和调用外部能力', { left: 790, top: 410, width: 330, height: 205 }, C.yellow, { titleColor: C.yellow, titleSize: 31, bodySize: 22, name: 'client' });
  arrow(s, 1140, 482, 120);
  panel(s, 'MCP Servers', 'GitHub · Notion · Database', { left: 1280, top: 370, width: 500, height: 285 }, C.blue, { titleColor: C.blue, titleSize: 31, bodySize: 25, name: 'servers' });
  panel(s, 'Tools · Resources · Prompts', '', { left: 760, top: 720, width: 540, height: 90 }, C.yellow, { titleColor: C.yellow, titleSize: 28, name: 'mcp-interfaces' });
  addNotes(s, 'MCP 是连接协议，不是 API 的替代品；它让 AI 应用以统一方式发现和调用工具。');
}

// 06 layers
{
  const s = deck.slides.add(); addFrame(s, 6, 'MCP 不取代 API，ADK 也不是另一种接口', 'LAYER RELATIONSHIP / 01:55');
  panel(s, 'ADK', 'Agent Development Kit\n\n状态 · 工作流 · 回调\n多 Agent · 评测', { left: 130, top: 350, width: 500, height: 340 }, C.yellow, { titleColor: C.yellow, titleSize: 43, bodySize: 24, name: 'adk' });
  panel(s, 'MCP', '统一发现和调用\n\nTools · Resources · Prompts', { left: 710, top: 350, width: 470, height: 340 }, C.blue, { titleColor: C.blue, titleSize: 43, bodySize: 24, name: 'mcp' });
  panel(s, 'API / SDK / CLI', '真正执行能力\n\n数据库 · 文件 · 服务', { left: 1260, top: 350, width: 500, height: 340 }, C.green, { titleColor: C.green, titleSize: 36, bodySize: 24, name: 'access' });
  panel(s, 'MCP 解决“怎么接工具” · ADK 解决“怎么组织 Agent”', '', { left: 320, top: 755, width: 1280, height: 100 }, C.blue, { titleSize: 29, name: 'layer-summary' });
  addNotes(s, '这一页解决最容易混淆的层级关系：MCP 在连接层，ADK 在 Agent 编排层。');
}

// 07 case
{
  const s = deck.slides.add(); addFrame(s, 7, '一个订单案例串起全部层级', 'CASE / 02:20');
  panel(s, '用户', '查订单 123\n未发货就退款', { left: 100, top: 390, width: 310, height: 190 }, C.yellow, { titleColor: C.yellow, titleSize: 31, bodySize: 24, name: 'user' }); arrow(s, 425, 465, 120);
  panel(s, 'ADK', '组织流程', { left: 560, top: 390, width: 300, height: 190 }, C.blue, { titleSize: 31, bodySize: 26, name: 'adk-case' }); arrow(s, 875, 465, 120);
  panel(s, 'LLM', '通过 Tool Calling\n选择查询工具', { left: 1010, top: 390, width: 340, height: 190 }, C.blue, { titleSize: 31, bodySize: 24, name: 'llm-case' }); arrow(s, 1365, 465, 120);
  panel(s, 'MCP / SDK / API', '读取订单数据库\n返回 pending\n执行 refund', { left: 1490, top: 340, width: 300, height: 310 }, C.green, { titleColor: C.green, titleSize: 25, bodySize: 23, name: 'stack-case' });
  panel(s, '退款完成 → 返回用户', '', { left: 520, top: 735, width: 880, height: 95 }, C.green, { titleColor: C.green, titleSize: 31, name: 'result-case' });
  addNotes(s, '订单案例把七个概念放到一条真实调用链中，强调它们不是互相替代。');
}

// 08 memory
{
  const s = deck.slides.add(); addFrame(s, 8, '七句话，记住它们的位置', 'MEMORY / 02:50');
  const defs = [
    ['API', '软件之间的能力契约'], ['SDK', '让开发者更方便地使用 API'], ['CLI', '让人或脚本通过命令行操作软件'],
    ['Function Calling', '让模型产生结构化函数请求'], ['Tool Calling', '模型选择并使用外部能力的总机制'], ['MCP', '让 AI 用统一协议连接工具和数据'], ['ADK', '把模型、工具、状态和流程组织成完整 Agent'],
  ];
  defs.forEach(([a,b], i) => { const y=275+i*75; box(s, 'line', { left: 150, top: y+62, width: 1620, height: 0 }, 'none', '#1C4462', 1); text(s, a, { left: 160, top: y, width: 400, height: 54 }, { fontSize: a.length > 12 ? 24 : 29, color: i===5 ? C.yellow : C.blue, bold: true }); text(s, b, { left: 590, top: y, width: 1120, height: 54 }, { fontSize: 25, color: C.gray }); });
  addNotes(s, '每个词只保留一句核心定义，作为后续课程的记忆卡。');
}

// 09 close
{
  const s = deck.slides.add(); addFrame(s, 9, '以后先问：它属于哪一层？', 'CLOSE / 03:14');
  panel(s, '01', '它属于哪一层？', { left: 135, top: 380, width: 430, height: 180 }, C.blue, { titleSize: 30, bodySize: 29, name: 'q1' });
  panel(s, '02', '它连接的是谁？', { left: 745, top: 380, width: 430, height: 180 }, C.yellow, { titleColor: C.yellow, titleSize: 30, bodySize: 29, name: 'q2' });
  panel(s, '03', '解决调用、连接，还是编排？', { left: 1355, top: 380, width: 430, height: 180 }, C.green, { titleColor: C.green, titleSize: 30, bodySize: 25, name: 'q3' });
  panel(s, '放回这张地图，AI Agent 技术栈就清楚了。', '', { left: 330, top: 720, width: 1260, height: 110 }, C.blue, { titleSize: 31, name: 'final' });
  addNotes(s, '回到开场问题，用三个判断问题收束。审核通过后再进入配音和词级对齐。');
}

for (const [index, slide] of deck.slides.items.entries()) {
  const stem = `slide-${String(index + 1).padStart(2, '0')}`;
  await writeBlob(`${QA}\\${stem}.png`, await deck.export({ slide, format: 'png', scale: 1 }));
  await fs.writeFile(`${QA}\\${stem}.layout.json`, await (await slide.export({ format: 'layout' })).text());
}
await writeBlob(`${QA}\\deck-montage.webp`, await deck.export({ format: 'webp', montage: true, scale: 1 }));
const pptx = await PresentationFile.exportPptx(deck);
await pptx.save(`${OUT}AgentTechStack_review.pptx`);
console.log(`${OUT}AgentTechStack_review.pptx`);
