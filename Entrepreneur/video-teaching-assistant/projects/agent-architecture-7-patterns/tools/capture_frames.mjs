import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { pathToFileURL } from "node:url";

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
if (!url || !output || !duration || !chrome || !puppeteerPath) {
  throw new Error("Usage: node capture_frames.mjs --url URL --output DIR --duration SEC --chrome PATH --composition-id ID (PUPPETEER_CORE_PATH required)");
}

const { default: puppeteer } = await import(pathToFileURL(puppeteerPath).href);
console.log("puppeteer loaded");
await fs.mkdir(output, { recursive: true });
// Each capture gets an isolated profile. Reusing Chrome's default profile can
// fail with a silent exit code 0 when another capture left a lock behind.
const userDataDir = await fs.mkdtemp(path.join(process.env.TEMP || process.env.TMP || ".", "hf-capture-"));
const browser = await puppeteer.launch({ headless: true, executablePath: chrome, userDataDir, args: ["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox", "--no-first-run", "--no-default-browser-check", "--disable-background-networking", "--disable-component-update", "--autoplay-policy=no-user-gesture-required"] });
console.log("browser launched");
try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
    // Audio is the separately frozen timing truth and is merged after frames.
    // Do not make Chrome decode a full WAV for every visual-only screenshot.
    await page.setRequestInterception(true);
    page.on("request", request => {
      if (request.url().toLowerCase().endsWith(".wav")) request.abort();
      else request.continue();
    });
  console.log("navigating", url);
  // The narration WAV is intentionally not awaited by the capture pass. The
  // timeline is seek-driven and audio timing is already frozen in the manifest;
  // waiting for networkidle0 can stall forever on a media request.
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 120000 });
  console.log("page loaded");
  await page.waitForFunction(() => window.gsap && window.__timelines, { timeout: 120000 });
  console.log("timeline loaded");
  const names = await page.evaluate(() => Object.keys(window.__timelines || {}));
  const timelineName = compositionId || names[0];
  if (!timelineName) throw new Error("No HyperFrames timeline found");
  // Set the timeline name before the first seek. The previous order performed
  // a seek against an undefined timeline on every frame, then sought again;
  // on long GSAP graphs that doubled work and could stall Chrome screenshots.
  await page.evaluate((name) => { window.__captureTimelineName = name; }, timelineName);
  const frameCount = Math.ceil(duration * fps);
  for (let i = 0; i < frameCount; i += 1) {
    const t = i / fps;
    await page.evaluate((time) => {
      const tl = window.__timelines?.[window.__captureTimelineName];
      if (tl) tl.seek(time, false);
      for (const el of document.querySelectorAll(".caption")) {
        const start = Number(el.dataset.start || 0);
        const end = start + Number(el.dataset.duration || 0);
        el.style.visibility = time >= start && time < end ? "visible" : "hidden";
      }
    }, t);
    const buffer = await page.screenshot({ type: "jpeg", quality: 90 });
    const filename = path.join(output, `frame_${String(i).padStart(6, "0")}.jpg`);
    await fs.writeFile(filename, buffer);
    if (i % Math.max(1, Math.floor(fps * 5)) === 0) console.log(`captured ${i + 1}/${frameCount} (${t.toFixed(2)}s)`);
  }
} finally {
  await browser.close();
}
