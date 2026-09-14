#!/usr/bin/env node

'use strict';

var fs = require('fs');
var path = require('path');
var vm = require('vm');

var ROOT = path.resolve(__dirname, '..');
var OUT = path.join(__dirname, 'designs');
var SIZE = 3000;

function loadPlaywright() {
  var candidates = [
    'playwright',
    '/tmp/opencode/merch/node_modules/playwright',
    '/tmp/opencode/qa2/node_modules/playwright'
  ];
  for (var i = 0; i < candidates.length; i++) {
    try {
      require.resolve(candidates[i]);
      return require(candidates[i]);
    } catch (e) {}
  }
  throw new Error('playwright not resolvable');
}

function loadTrades() {
  var src = fs.readFileSync(path.join(ROOT, 'js', 'quiz.js'), 'utf8');
  var marker = 'var TRADES = [';
  var start = src.indexOf(marker);
  if (start === -1) throw new Error('TRADES array not found in js/quiz.js');
  start += marker.length;
  var end = src.indexOf('];', start);
  if (end === -1) throw new Error('TRADES array close not found in js/quiz.js');
  return vm.runInNewContext('[' + src.slice(start, end) + ']');
}

function slugFor(name) {
  return name.toLowerCase().replace(/\s+/g, '-');
}

function ring() {
  return (
    '<circle cx="100" cy="100" r="97" fill="none" stroke="#FFFFFF" stroke-opacity="0.16" stroke-width="5"/>' +
    '<circle cx="100" cy="100" r="97" fill="none" stroke="#FFFFFF" stroke-opacity="0.9" stroke-width="2" stroke-dasharray="1 14" stroke-linecap="round"/>'
  );
}

function iconElectrician() {
  return (
    ring() +
    '<path d="M118 10 L46 116 h46 L72 190 L154 86 h-48 Z" fill="#FFFFFF"/>' +
    '<path d="M118 10 L46 116 h46 L72 190 L154 86 h-48 Z" fill="none" stroke="#FFFFFF" stroke-opacity="0.25" stroke-width="6" stroke-linejoin="round"/>'
  );
}

function iconPlumber() {
  return (
    ring() +
    '<g stroke-linecap="round" stroke-linejoin="round" fill="none" stroke="#FFFFFF" stroke-width="24">' +
    '<path d="M46 54 h30 c30 0 46 15 46 40 0 34 -26 54 -58 54 h-44"/>' +
    '</g>' +
    '<path d="M100 10 C86 34 79 44 79 55 a21 21 0 0 0 42 0 C121 44 114 34 100 10 Z" fill="#FFFFFF"/>'
  );
}

function iconWelder() {
  return (
    ring() +
    '<path d="M100 18 C56 72 40 102 40 128 a60 60 0 0 0 120 0 c0 -26 -16 -56 -60 -110 Z" fill="#FFFFFF"/>' +
    '<path d="M100 62 C75 96 65 114 65 132 a35 35 0 0 0 70 0 c0 -18 -10 -36 -35 -70 Z" fill="#0B0B10"/><path d="M100 74 C85 96 79 108 79 128 a21 21 0 0 0 42 0 c0 -20 -6 -32 -21 -54 Z" fill="#FFFFFF"/>'
  );
}

function iconHvac() {
  var parts = [ring()];
  for (var i = 0; i < 3; i++) {
    var rot = i * 60;
    parts.push(
      '<g transform="rotate(' + rot + ' 100 100)" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round">' +
        '<line x1="100" y1="28" x2="100" y2="172"/>' +
        '<line x1="78" y1="62" x2="122" y2="62"/>' +
        '<line x1="78" y1="138" x2="122" y2="138"/>' +
      '</g>'
    );
  }
  parts.push('<circle cx="100" cy="100" r="9" fill="#FFFFFF"/>');
  return parts.join('');
}

function iconAuto() {
  var parts = [ring()];
  for (var i = 0; i < 8; i++) {
    var rot = i * 45;
    parts.push('<rect x="88" y="14" width="24" height="56" rx="9" fill="#FFFFFF" transform="rotate(' + rot + ' 100 100)"/>');
  }
  parts.push('<circle cx="100" cy="100" r="48" fill="#FFFFFF"/>');
  parts.push('<circle cx="100" cy="100" r="20" fill="#0B0B10"/>');
  parts.push('<circle cx="100" cy="100" r="9" fill="#FFFFFF"/>');
  return parts.join('');
}

function iconCarpenter() {
  return (
    ring() +
    '<rect x="86" y="62" width="28" height="134" rx="10" fill="#FFFFFF"/>' +
    '<path d="M48 62 h104 v34 h-92 a26 26 0 0 1 -8 -16 Z" fill="#FFFFFF"/>' +
    '<path d="M48 78 l-14 20 a12 12 0 0 0 8 17 l8 -6 z" fill="#FFFFFF"/>' +
    '<path d="M150 150 h12 v36 h-12 z" fill="#FFFFFF"/><circle cx="156" cy="142" r="8" fill="#FFFFFF"/>'
  );
}

function iconIronworker() {
  return (
    ring() +
    '<path d="M46 30 h108 v30 h-34 v80 h34 v30 h-108 v-30 h34 v-80 h-34 z" fill="#FFFFFF"/>' +
    '<circle cx="58" cy="45" r="6" fill="#0000"/><circle cx="142" cy="45" r="6" opacity="0"/>' +
    '<path d="M100 6 v34 a24 24 0 0 0 48 0 v-18" fill="none" stroke="#FFFFFF" stroke-width="13" stroke-linecap="round"/>'
  );
}

function iconPipefitter() {
  return (
    ring() +
    '<rect x="26" y="88" width="148" height="26" rx="13" fill="#FFFFFF"/>' +
    '<rect x="88" y="26" width="26" height="148" rx="13" fill="#FFFFFF"/>' +
    '<circle cx="100" cy="100" r="34" fill="#0B0B10" stroke="#FFFFFF" stroke-width="12"/>' +
    '<circle cx="84" cy="84" r="5" fill="#FFFFFF"/><circle cx="116" cy="84" r="5" fill="#FFFFFF"/>' +
    '<circle cx="84" cy="116" r="5" fill="#FFFFFF"/><circle cx="116" cy="116" r="5" fill="#FFFFFF"/>'
  );
}

function iconDiesel() {
  return (
    ring() +
    '<rect x="16" y="78" width="128" height="46" rx="8" fill="#FFFFFF"/>' +
    '<path d="M136 60 h44 v24 h20 v40 h-64 z" fill="#FFFFFF"/>' +
    '<rect x="146" y="66" width="26" height="20" rx="4" fill="#0B0B10"/>' +
    '<circle cx="70" cy="138" r="20" fill="#FFFFFF"/><circle cx="70" cy="138" r="9" fill="#0B0B10"/>' +
    '<circle cx="166" cy="138" r="20" fill="#FFFFFF"/><circle cx="166" cy="138" r="9" fill="#0B0B10"/>'
  );
}

function iconMason() {
  return (
    ring() +
    '<rect x="32" y="120" width="136" height="48" rx="6" fill="#FFFFFF"/>' +
    '<rect x="96" y="120" width="6" height="48" fill="#0B0B10" opacity="0"/>' +
    '<path d="M100 60 L148 108 L100 156 L52 108 Z" fill="#FFFFFF"/>' +
    '<rect x="88" y="26" width="24" height="40" rx="8" fill="#FFFFFF"/>' +
    '<line x1="66" y1="132" x2="134" y2="132" stroke="#0B0B10" stroke-width="6" opacity="0.35"/>' +
    '<line x1="100" y1="120" x2="100" y2="168" stroke="#0B0B10" stroke-width="6" opacity="0.35"/>'
  );
}

function iconRoofer() {
  return (
    ring() +
    '<path d="M24 118 L100 38 L176 118 Z" fill="#FFFFFF"/>' +
    '<path d="M60 104 L100 66 L140 104" fill="none" stroke="#0B0B10" stroke-width="7" stroke-linecap="round" opacity="0.35"/>' +
    '<path d="M82 118 L100 102 L118 118" fill="none" stroke="#0B0B10" stroke-width="6" stroke-linecap="round" opacity="0.3"/>' +
    '<circle cx="160" cy="48" r="20" fill="#FFFFFF"/><circle cx="160" cy="48" r="20" fill="none" stroke="#0B0B10" stroke-width="6" opacity="0.35"/>'
  );
}

function iconCm() {
  return (
    ring() +
    '<g transform="rotate(-8 100 100)">' +
      '<rect x="42" y="58" width="116" height="82" rx="6" fill="#FFFFFF"/>' +
      '<line x1="70" y1="66" x2="70" y2="132" stroke="#0B0B10" stroke-width="7" opacity="0.22"/>' +
      '<line x1="42" y1="96" x2="158" y2="96" stroke="#0B0B10" stroke-width="7" opacity="0.22"/>' +
      '<circle cx="120" cy="82" r="14" fill="none" stroke="#0B0B10" stroke-width="7" opacity="0.28"/>' +
      '<path d="M120 70 L128 82 L120 94 L112 82 Z" fill="#0B0B10" opacity="0.28"/>' +
    '</g>' +
    '<path d="M56 128 a44 44 0 0 1 88 0 Z" fill="#FFFFFF"/>' +
    '<rect x="36" y="126" width="128" height="16" rx="8" fill="#FFFFFF"/>' +
    '<rect x="90" y="70" width="20" height="38" rx="6" fill="#FFFFFF"/>' +
    '<path d="M58 118 a36 36 0 0 1 20 -6" fill="none" stroke="#0B0B10" stroke-width="5" opacity="0.28" stroke-linecap="round"/>'
  );
}

var ICONS = {
  electrician: iconElectrician,
  plumber: iconPlumber,
  welder: iconWelder,
  'hvac-technician': iconHvac,
  'automotive-mechanic': iconAuto,
  carpenter: iconCarpenter,
  ironworker: iconIronworker,
  pipefitter: iconPipefitter,
  'diesel-mechanic': iconDiesel,
  mason: iconMason,
  roofer: iconRoofer,
  'construction-manager': iconCm
};

var DESIGNS = [
  { slug: 'electrician', name: 'Electrician', color: '#FFC400', kicker: 'ELECTRICAL', slogan: ['HIGH VOLTAGE,', 'ZERO DEGREES'] },
  { slug: 'plumber', name: 'Plumber', color: '#00B8D4', kicker: 'PLUMBING', slogan: ['FLUSH', 'WITH CASH'] },
  { slug: 'welder', name: 'Welder', color: '#FF6D00', kicker: 'WELDING', slogan: ['HOT PAY,', 'COOL JOB'] },
  { slug: 'hvac-technician', name: 'HVAC Technician', color: '#3FA9E3', kicker: 'HVAC', slogan: ['CHILL WORK,', 'WARM PAYCHECKS'] },
  { slug: 'automotive-mechanic', name: 'Automotive Mechanic', color: '#E53935', kicker: 'AUTOMOTIVE', slogan: ['GREASY HANDS,', 'FAT PAYCHECKS'] },
  { slug: 'carpenter', name: 'Carpenter', color: '#D9932F', kicker: 'CARPENTRY', slogan: ['MEASURE TWICE,', 'GET PAID ONCE'] },
  { slug: 'ironworker', name: 'Ironworker', color: '#5C6BC0', kicker: 'IRONWORK', slogan: ['COWBOY OF', 'THE SKY'] },
  { slug: 'pipefitter', name: 'Pipefitter', color: '#9C27B0', kicker: 'PIPEFITTING', slogan: ['STRAIGHT PIPES,', 'STRONG PAY'] },
  { slug: 'diesel-mechanic', name: 'Diesel Mechanic', color: '#7CB342', kicker: 'DIESEL', slogan: ['BIG RIGS,', 'BIG BUCKS'] },
  { slug: 'mason', name: 'Mason', color: '#B4532E', kicker: 'MASONRY', slogan: ['ROCK SOLID,', 'BUILT TO LAST'] },
  { slug: 'roofer', name: 'Roofer', color: '#26A69A', kicker: 'ROOFING', slogan: ['RAIN OR SHINE,', 'WE CLIMB'] },
  { slug: 'construction-manager', name: 'Construction Manager', color: '#E65100', kicker: 'CONSTRUCTION', slogan: ['FROM TOOLBOX', 'TO SIX FIGURES'] }
];

function esc(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function buildSVG(d) {
  var nameSize = Math.min(230, Math.max(118, 2080 / (0.78 * d.name.length)));
  var nameSpacing = d.name.length > 14 ? 7 : 14;
  var icon = ICONS[d.slug] ? ICONS[d.slug]() : ring();
  var slogan = '';
  var sy = d.slogan.length === 2 ? 2396 : 2488;
  for (var i = 0; i < d.slogan.length; i++) {
    slogan += '<text x="1500" y="' + (sy + i * 188) + '" text-anchor="middle" font-family="DejaVu Sans,Arial,sans-serif" font-weight="700" font-size="152" fill="' + d.color + '" letter-spacing="16">' + esc(d.slogan[i]) + '</text>';
  }
  return (
    '<svg xmlns="http://www.w3.org/2000/svg" width="' + SIZE + '" height="' + SIZE + '" viewBox="0 0 ' + SIZE + ' ' + SIZE + '">' +
    '<defs>' +
      '<radialGradient id="glow" cx="0.5" cy="0.42" r="0.5">' +
        '<stop offset="0" stop-color="' + d.color + '" stop-opacity="0.16"/>' +
        '<stop offset="0.5" stop-color="' + d.color + '" stop-opacity="0.05"/>' +
        '<stop offset="1" stop-color="' + d.color + '" stop-opacity="0"/>' +
      '</radialGradient>' +
      '<linearGradient id="slab" x1="0" y1="0" x2="1" y2="1">' +
        '<stop offset="0" stop-color="#1D1D26"/>' +
        '<stop offset="0.5" stop-color="#17171E"/>' +
        '<stop offset="1" stop-color="#101016"/>' +
      '</linearGradient>' +
    '</defs>' +
    '<rect x="300" y="300" width="2400" height="2400" rx="380" fill="url(#slab)"/>' +
    '<rect x="300" y="300" width="2400" height="2400" rx="380" fill="url(#glow)"/>' +
    '<rect x="352" y="352" width="2296" height="2296" rx="340" fill="none" stroke="' + d.color + '" stroke-width="16" stroke-opacity="0.85"/>' +
    '<rect x="372" y="372" width="2256" height="2256" rx="320" fill="none" stroke="#FFFFFF" stroke-opacity="0.14" stroke-width="6"/>' +
    '<g transform="translate(1140,700) scale(3.6)">' + icon + '</g>' +
    '<text x="1500" y="1866" text-anchor="middle" font-family="DejaVu Sans,Arial,sans-serif" font-weight="700" font-size="72" fill="#EDEDED" fill-opacity="0.6" letter-spacing="26">' + esc(d.kicker) + '</text>' +
    '<text x="1500" y="2096" text-anchor="middle" font-family="DejaVu Sans,Arial,sans-serif" font-weight="700" font-size="' + nameSize + '" fill="#FFFFFF" letter-spacing="' + nameSpacing + '">' + esc(d.name.toUpperCase()) + '</text>' +
    '<rect x="' + (1500 - Math.min(860, nameSize * 0.72 * d.name.length)) + '" y="2230" width="' + (Math.min(1720, nameSize * 1.44 * d.name.length)) + '" height="18" rx="9" fill="' + d.color + '"/>' +
    slogan +
    '<text x="1500" y="2634" text-anchor="middle" font-family="DejaVu Sans,Arial,sans-serif" font-weight="700" font-size="44" fill="#FFFFFF" fill-opacity="0.35" letter-spacing="18">T R A D E L I F T</text>' +
    '</svg>'
  );
}

function readPNGSize(buf) {
  if (buf.length < 24 || buf.readUInt32BE(0) !== 0x89504e47) return null;
  return { w: buf.readUInt32BE(16), h: buf.readUInt32BE(20) };
}

async function main() {
  var playwright = loadPlaywright();
  var trades = loadTrades();
  var slugs = trades.map(function (t) { return slugFor(t.name); });
  var designSlugs = DESIGNS.map(function (d) { return d.slug; });
  var missing = slugs.filter(function (s) { return designSlugs.indexOf(s) === -1; });
  var extra = designSlugs.filter(function (s) { return slugs.indexOf(s) === -1; });
  if (missing.length || extra.length) {
    throw new Error('slugs mismatch -> quiz missing: ' + missing.join(',') + ' | designs extra: ' + extra.join(','));
  }
  fs.mkdirSync(OUT, { recursive: true });

  var browser = await playwright.chromium.launch();
  var context = await browser.newContext({ viewport: { width: SIZE, height: SIZE }, deviceScaleFactor: 1 });
  var page = await context.newPage();

  var results = [];
  for (var i = 0; i < DESIGNS.length; i++) {
    var d = DESIGNS[i];
    var svg = buildSVG(d);
    var svgPath = path.join(OUT, d.slug + '.svg');
    var pngPath = path.join(OUT, d.slug + '.png');
    fs.writeFileSync(svgPath, svg);

    await page.setContent(
      '<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:transparent;}</style></head><body>' + svg + '</body></html>',
      { waitUntil: 'load' }
    );
    await page.screenshot({ path: pngPath, clip: { x: 0, y: 0, width: SIZE, height: SIZE }, omitBackground: true });

    var buf = fs.readFileSync(pngPath);
    var dims = readPNGSize(buf);
    var size = fs.statSync(pngPath).size;
    var ok = dims && dims.w === SIZE && dims.h === SIZE && size > 150 * 1024;
    results.push({ slug: d.slug, name: d.name, dims: dims, size: size, ok: ok });
    console.log(
      d.name.padEnd(22) + d.slug.padEnd(24) +
      (dims ? dims.w + 'x' + dims.h : 'BAD PNG').padEnd(14) +
      Math.round(size / 1024) + 'KB ' + (ok ? 'PASS' : 'FAIL')
    );
  }

  await browser.close();
  var failed = results.filter(function (r) { return !r.ok; });
  if (failed.length) {
    console.error('FAILED: ' + failed.map(function (f) { return f.slug; }).join(', '));
    process.exit(1);
  }
  console.log('OK: ' + results.length + ' designs -> merch/designs/');
}

main().catch(function (err) {
  console.error(err);
  process.exit(1);
});