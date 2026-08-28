import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

function getAttribute(tag, name) {
  const match = tag.match(
    new RegExp(`\\b${name}\\s*=\\s*(?:"([^"]*)"|'([^']*)'|([^\\s>]+))`, "i"),
  );
  return match?.[1] ?? match?.[2] ?? match?.[3] ?? null;
}

test("preflight places the course PDF download before its hero", async () => {
  const outputPath = new URL(
    "../docs/.vitepress/dist/preflight/index.html",
    import.meta.url,
  );
  const html = await readFile(outputPath, "utf8");
  const mainStart = html.indexOf("<main");
  const mainEnd = html.indexOf("</main>", mainStart);
  const main = html.slice(mainStart, mainEnd);
  const pageTitle = main.match(/<h1\b[^>]*>[\s\S]*?AI Builder Camp[\s\S]*?<\/h1>/i);
  const callout = main.match(/<a\b[^>]*class="resource-callout"[^>]*>[\s\S]*?<\/a>/i);

  assert.ok(pageTitle, "expected the preflight page title");
  assert.ok(callout, "expected a course download callout");

  const openingTag = callout[0].match(/^<a\b[^>]*>/i)?.[0] ?? "";
  assert.equal(
    getAttribute(openingTag, "href"),
    "https://empowerwithai.camp/abce/downloads/3hour-ai-digital-employee-course-v2.pdf",
  );
  assert.equal(getAttribute(openingTag, "target"), "_blank");
  assert.deepEqual(
    (getAttribute(openingTag, "rel") ?? "").split(/\s+/).sort(),
    ["noopener", "noreferrer"],
  );
  assert.match(callout[0], /下载《3小时 AI 数字员工课程 V2》课件/);

  const titleEnd = pageTitle.index + pageTitle[0].length;
  const calloutIndex = main.indexOf(callout[0]);
  const heroIndex = main.indexOf('<div class="doc-hero dark">');
  assert.ok(calloutIndex >= titleEnd, "expected the download after the page title");
  assert.ok(heroIndex > calloutIndex, "expected the download before the hero");
});
