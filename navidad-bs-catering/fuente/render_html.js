// Renderiza páginas HTML a PDF (y opcionalmente PNG) a partir de una lista JSON.
// Uso: node fuente/render_html.js trabajos.json
// Cada trabajo: { html, pdf, png?, w, h, pngScale? }   (w y h en mm; omitir w/h usa @page del HTML)
const { chromium } = require('playwright');
const fs = require('fs');

const MM = 96 / 25.4;

(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch();
  for (const j of jobs) {
    const vw = j.w ? Math.ceil(j.w * MM) : 1200;
    const vh = j.h ? Math.ceil(j.h * MM) : 1600;
    const ctx = await browser.newContext({ viewport: { width: vw, height: vh },
                                           deviceScaleFactor: j.pngScale || 1 });
    const page = await ctx.newPage();
    await page.goto('file://' + j.html);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(150);
    const opts = { path: j.pdf, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } };
    if (j.w) { opts.width = `${j.w}mm`; opts.height = `${j.h}mm`; } else { opts.preferCSSPageSize = true; }
    await page.pdf(opts);
    if (j.png) await page.screenshot({ path: j.png, fullPage: true });
    await ctx.close();
    console.log('ok', j.pdf.split('/').pop());
  }
  await browser.close();
})();
