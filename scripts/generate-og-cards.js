#!/usr/bin/env node

'use strict';

var fs = require('fs');
var path = require('path');
var vm = require('vm');

var ROOT = path.resolve(__dirname, '..');
var CARD_W = 1200;
var CARD_H = 630;

function loadPlaywright() {
  try {
    require.resolve('playwright');
    return require('playwright');
  } catch (e) {
    return require('/tmp/opencode/qa2/node_modules/playwright');
  }
}

function loadTrades() {
  var src = fs.readFileSync(path.join(ROOT, 'js', 'quiz.js'), 'utf8');
  var marker = 'var TRADES = [';
  var start = src.indexOf(marker);
  if (start === -1) throw new Error('TRADES array not found in js/quiz.js');
  start += marker.length;
  var end = src.indexOf('];', start);
  if (end === -1) throw new Error('TRADES array close not found in js/quiz.js');
  var arraySrc = src.slice(start, end);
  return vm.runInNewContext('[' + arraySrc + ']');
}

function esc(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function buildCardHTML(trade) {
  return (
    '<!doctype html><html><head><meta charset="utf-8">' +
    '<style>html{font-size:16px}body{margin:0;padding:0;background:#0a0a0a;}' +
    '.tl-card{width:' + CARD_W + 'px;height:' + CARD_H + 'px;background:linear-gradient(145deg,#0a0a0a 0%,#1a0f00 35%,#2a1500 65%,#0a0a0a 100%);display:flex;flex-direction:column;justify-content:space-between;padding:52px 60px 44px;box-sizing:border-box;position:relative;}' +
    '.tl-overlay{position:absolute;top:0;left:0;width:100%;height:100%;background:radial-gradient(circle at 85% 20%,rgba(255,107,0,0.07) 0%,transparent 50%),radial-gradient(circle at 15% 80%,rgba(255,193,7,0.04) 0%,transparent 40%);pointer-events:none;}' +
    '.tl-body{position:relative;z-index:1;display:flex;align-items:flex-start;justify-content:space-between;}' +
    '.tl-left{flex:1;}' +
    '.tl-icon-hero{font-size:5rem;line-height:1;margin-bottom:20px;}' +
    '.tl-eyebrow{font-size:1.1rem;font-weight:600;color:#ff6b00;letter-spacing:3px;text-transform:uppercase;margin-bottom:10px;}' +
    '.tl-h1{font-size:44px;font-weight:900;color:#ffffff;line-height:1.05;margin:0 0 6px;}' +
    '.tl-h2{font-size:56px;font-weight:900;color:#ff6b00;line-height:1.05;margin:0 0 16px;}' +
    '.tl-salary{display:inline-block;padding:8px 22px;background:rgba(255,193,7,0.1);border:1px solid rgba(255,193,7,0.3);border-radius:50px;font-size:1.15rem;font-weight:700;color:#ffc107;}' +
    '.tl-tile{flex-shrink:0;width:180px;height:180px;border-radius:16px;background:rgba(255,107,0,0.08);border:1px solid rgba(255,107,0,0.2);display:flex;align-items:center;justify-content:center;font-size:6rem;align-self:center;}' +
    '.tl-footer{position:relative;z-index:1;display:flex;align-items:center;justify-content:space-between;border-top:1px solid #2a2a2a;padding-top:24px;}' +
    '.tl-brand{display:flex;align-items:center;gap:10px;}' +
    '.tl-brand-icon{font-size:1.6rem;}' +
    '.tl-brand-name{font-size:1.4rem;font-weight:800;color:#ffffff;}' +
    '.tl-cta{font-size:0.9rem;color:#8a8a8a;}' +
    '</style></head><body>' +
    '<div class="tl-card">' +
      '<div class="tl-overlay"></div>' +
      '<div class="tl-body">' +
        '<div class="tl-left">' +
          '<div class="tl-icon-hero">' + esc(trade.icon) + '</div>' +
          '<div class="tl-eyebrow">Your Trade Match</div>' +
          '<div class="tl-h1">I\'m built for</div>' +
          '<div class="tl-h2">' + esc(trade.name) + '!</div>' +
          '<div class="tl-salary">Average Salary: ' + esc(trade.salary) + '</div>' +
        '</div>' +
        '<div class="tl-tile">' + esc(trade.icon) + '</div>' +
      '</div>' +
      '<div class="tl-footer">' +
        '<div class="tl-brand">' +
          '<span class="tl-brand-icon">⚒️</span>' +
          '<span class="tl-brand-name">TradeLift</span>' +
        '</div>' +
        '<div class="tl-cta">Take the quiz → https://pablo63leiva-alt.github.io/tradelift/quiz.html</div>' +
      '</div>' +
    '</div>' +
    '</body></html>'
  );
}

function slugFor(name) {
  return name.toLowerCase().replace(/\s+/g, '-');
}

async function main() {
  var playwright = loadPlaywright();
  var trades = loadTrades();
  var outDir = path.join(ROOT, 'img');
  fs.mkdirSync(outDir, { recursive: true });

  var browser = await playwright.chromium.launch();
  var context = await browser.newContext({ viewport: { width: CARD_W, height: CARD_H }, deviceScaleFactor: 1 });
  var page = await context.newPage();

  console.log('trade'.padEnd(24) + 'headline'.padEnd(22) + 'salary'.padEnd(16) + 'assertion'.padEnd(10) + 'file');
  var results = [];

  for (var i = 0; i < trades.length; i++) {
    var trade = trades[i];
    var slug = slugFor(trade.name);
    var outPath = path.join(outDir, 'og-' + slug + '.png');
    var html = buildCardHTML(trade);

    await page.setContent(html, { waitUntil: 'load' });
    await page.screenshot({ path: outPath, clip: { x: 0, y: 0, width: CARD_W, height: CARD_H } });

    var headline = await page.evaluate(function (name) {
      var h2 = document.querySelector('.tl-h2');
      return h2 ? h2.textContent.trim() : '';
    }, trade.name);
    var salaryText = await page.evaluate(function () {
      var el = document.querySelector('.tl-salary');
      return el ? el.textContent.trim() : '';
    }, null);
    var bodyText = await page.evaluate(function () {
      return document.body.innerText;
    });

    var okHeadline = headline.indexOf(trade.name) !== -1;
    var okSalary = bodyText.indexOf(trade.salary) !== -1 && salaryText.indexOf(trade.salary) !== -1;
    var size = fs.statSync(outPath).size;

    results.push({ name: trade.name, slug: slug, headline: headline, salary: trade.salary, ok: okHeadline && okSalary, size: size });
    console.log(
      trade.name.padEnd(24) + headline.padEnd(22) + trade.salary.padEnd(16) +
      (okHeadline && okSalary ? 'PASS' : 'FAIL').padEnd(10) + 'og-' + slug + '.png (' + size + ' bytes)'
    );
  }

  await browser.close();

  var failed = results.filter(function (r) { return !r.ok; });
  if (failed.length) {
    console.error('FAILED assertions: ' + failed.map(function (f) { return f.name; }).join(', '));
    process.exit(1);
  }
  console.log('Generated ' + results.length + ' OG cards -> img/og-<slug>.png');
  process.exit(0);
}

main().catch(function (err) {
  console.error(err);
  process.exit(1);
});