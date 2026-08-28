import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

test("demo overview renders its three card titles as text instead of links", async () => {
  const outputPath = new URL(
    "../docs/.vitepress/dist/demos/index.html",
    import.meta.url,
  );
  const html = await readFile(outputPath, "utf8");
  const demoGrid = html.match(/<div class="demo-grid">([\s\S]*?)<\/div>/i)?.[1];

  assert.ok(demoGrid, "expected the built demos page to contain a demo grid");

  const cardTitles = [...demoGrid.matchAll(/<h3\b[^>]*>([\s\S]*?)<\/h3>/gi)];
  assert.equal(cardTitles.length, 3, "expected exactly three demo card titles");

  for (const [, titleMarkup] of cardTitles) {
    assert.doesNotMatch(titleMarkup, /<a\b/i);
  }
});
