import fs from 'node:fs';
const html = fs.readFileSync(new URL('../hyperframes/index.html', import.meta.url), 'utf8');
const required = [
  'data-composition-id="mcp-api-cli-review"',
  'data-width="1920"',
  'data-height="1080"',
  'data-duration="210"',
  'data-subtitle-safe-band="900-1080"',
  "window.__timelines['mcp-api-cli-review']",
];
const clips = (html.match(/class="clip"/g) || []).length;
const missing = required.filter((item) => !html.includes(item));
const status = missing.length === 0 && clips === 9 ? 'pass' : 'fail';
console.log(JSON.stringify({ clips, missing, status }, null, 2));
process.exitCode = status === 'pass' ? 0 : 1;

