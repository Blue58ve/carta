// Convierte las páginas de fuente/_build en PDF (impresión y guías) y PNG (vista previa).
// Uso: node fuente/render.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const BUILD = path.join(__dirname, '_build');
const MM = 96 / 25.4; // px CSS por mm
const PX_PER_MM = 20;  // resolución de las vistas previas

(async () => {
  const manifest = JSON.parse(fs.readFileSync(path.join(BUILD, 'manifest.json'), 'utf8'));
  const browser = await chromium.launch();
  const outDirs = ['impresion', 'guias', 'vista-previa'].map(d => path.join(ROOT, d));
  outDirs.forEach(d => fs.mkdirSync(d, { recursive: true }));

  for (const [i, p] of manifest.entries()) {
    const n = String(i + 1).padStart(2, '0');
    for (const [mode, job] of Object.entries(p.jobs)) {
      const ctx = await browser.newContext({
        viewport: { width: Math.ceil(job.w * MM), height: Math.ceil(job.h * MM) },
        deviceScaleFactor: mode.startsWith('preview') ? PX_PER_MM / MM : 8 / MM,
      });
      const page = await ctx.newPage();
      await page.goto('file://' + job.html);
      await page.evaluate(() => document.fonts.ready);
      if (mode === 'print') {
        await page.pdf({
          path: path.join(ROOT, 'impresion', `${n}-${p.id}.pdf`),
          width: `${job.w}mm`, height: `${job.h}mm`, printBackground: true,
          margin: { top: 0, right: 0, bottom: 0, left: 0 },
        });
      } else if (mode === 'guide') {
        await page.pdf({
          path: path.join(ROOT, 'guias', `${n}-${p.id}-guia.pdf`),
          width: `${job.w}mm`, height: `${job.h}mm`, printBackground: true,
          margin: { top: 0, right: 0, bottom: 0, left: 0 },
        });
        await page.screenshot({ path: path.join(ROOT, 'guias', `${n}-${p.id}-guia.png`), fullPage: true });
      } else {
        const suffix = mode === 'preview' ? '' : '-' + mode.replace('preview-', '');
        await page.screenshot({
          path: path.join(ROOT, 'vista-previa', `${p.id}${suffix}.png`),
          omitBackground: true,
          clip: { x: 0, y: 0, width: job.w * MM, height: job.h * MM },
        });
      }
      await ctx.close();
    }
    console.log('ok', n, p.id);
  }
  await browser.close();
})();
