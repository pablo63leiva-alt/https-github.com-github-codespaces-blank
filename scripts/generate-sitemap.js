#!/usr/bin/env node

var fs = require('fs');
var path = require('path');
var execSync = require('child_process').execSync;

var SITE_URL = 'https://tradelift.surge.sh';
var ROOT = path.resolve(__dirname, '..');
var mainPages = ['index.html', 'trades.html', 'getting-started.html', 'resources.html', 'blog.html', 'tools.html', 'quiz.html', 'badge.html'];
var blogPosts = fs.readdirSync(path.join(ROOT, 'blog'))
  .filter(function (f) { return /\.html$/.test(f); })
  .sort()
  .map(function (f) { return 'blog/' + f; });
var pages = mainPages.filter(function (f) {
  try { fs.statSync(path.join(ROOT, f)); return true; } catch (_) { return false; }
});
var posts = blogPosts.filter(function (f) {
  try { fs.statSync(path.join(ROOT, f)); return true; } catch (_) { return false; }
});

var allPages = pages.concat(posts);

var urls = allPages.map(function (file) {
  var loc = SITE_URL + '/' + file;
  var filePath = path.join(ROOT, file);
  var lastmod;
  try {
    var raw = execSync('git log -1 --format=%ci -- ' + filePath, { cwd: ROOT })
      .toString()
      .trim();
    if (raw) {
      lastmod = raw.split(' ')[0];
    } else {
      lastmod = new Date().toISOString().split('T')[0];
    }
  } catch (_) {
    lastmod = new Date().toISOString().split('T')[0];
  }
  var priority;
  if (file === 'index.html') { priority = '1.0'; }
  else if (file.indexOf('blog/') === 0) { priority = '0.6'; }
  else { priority = '0.7'; }
  return '  <url>\n    <loc>' + loc + '</loc>\n    <lastmod>' + lastmod + '</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>' + priority + '</priority>\n  </url>';
});

var xml = '<?xml version="1.0" encoding="UTF-8"?>\n' +
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  urls.join('\n') + '\n' +
  '</urlset>\n';

var outPath = path.join(ROOT, 'sitemap.xml');
fs.writeFileSync(outPath, xml);
console.log('sitemap.xml written with ' + urls.length + ' URLs');
