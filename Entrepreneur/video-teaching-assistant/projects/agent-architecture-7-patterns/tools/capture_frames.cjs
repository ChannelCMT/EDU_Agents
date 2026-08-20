const fs = require("node:fs");
const path = require("node:path");
const process = require("node:process");

function arg(name, fallback = null) {
  const i = process.argv.indexOf(name);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const url = arg("--url");
const output = arg("--output");
const duration = Number(arg("--duration", "0"));
const fps = Number(arg("--fps", "30"));
const chrome = arg("--chrome");
const compositionId = arg("--composition-id");
const puppeteerPath = process.env.PUPPETEER_CORE_PATH;
if (!url || !output || !duration || !chrome || !puppeteerPath) throw new Error("missing capture arguments");
const puppeteer = require(puppeteerPath);
console.log("puppeteer loaded");
fs.mkdirSync(output, { recursive: true });
(async () => {
  const browser = await puppeteer.launch({ headless: true, executablePath: chrome, args: ["--disable-gpu", "--no-sandbox", "--autoplay-policy=no-user-gesture-required"] });
  console.log("browser launched");
  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
    console.log("navigating", url);
    await page.goto(url, { waitUntil: "networkidle0", timeout: 120000 });
    console.log("page loaded");
    await page.waitForFunction(() => window.gsap && window.__timelines, { timeout: 120000 });
    console.log("timeline loaded");
    const names = await page.evaluate(() => Object.keys(window.__timelines || {}));
    const timelineName = compositionId || names[0];
    const frameCount = Math.ceil(duration * fps);
    for (let i = 0; i < frameCount; i += 1) {
      const t = i / fps;
      await page.evaluate((name) => { window.__captureTimelineName = name; }, timelineName);
      await page.evaluate((time) => {
        window.__timelines?.[window.__captureTimelineName]?.seek(time, false);
        for (const el of document.querySelectorAll(".clip:not(.caption)")) {
          const start = Number(el.dataset.start || 0);
          const end = start + Number(el.dataset.duration || 0);
          el.style.visibility = time >= start && time < end ? "visible" : "hidden";
        }
        for (const el of document.querySelectorAll(".caption")) {
          const start = Number(el.dataset.start || 0);
          const end = start + Number(el.dataset.duration || 0);
          el.style.visibility = time >= start && time < end ? "visible" : "hidden";
        }
      }, t);
      const buffer = await page.screenshot({ type: "jpeg", quality: 90 });
      fs.writeFileSync(path.join(output, `frame_${String(i).padStart(6, "0")}.jpg`), buffer);
      if (i % Math.max(1, Math.floor(fps * 5)) === 0) console.log(`captured ${i + 1}/${frameCount} (${t.toFixed(2)}s)`);
    }
  } finally {
    await browser.close();
  }
})().catch((error) => { console.error(error); process.exitCode = 1; });
