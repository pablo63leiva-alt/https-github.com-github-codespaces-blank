(function () {
  'use strict';

  var CARD_W = 1200;
  var CARD_H = 630;
  var DEFAULT_DOWNLOAD_LABEL = 'Download My Result Card';
  var previewEl = null;
  var downloadBtn = null;
  var currentTrade = null;

  function esc(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function readCurrentResult() {
    var tradeEl = document.getElementById('quiz-results-trade');
    if (!tradeEl || tradeEl.closest('[hidden]')) return null;
    var name = tradeEl.getAttribute('data-trade');
    if (!name) return null;
    var salaryEl = document.getElementById('quiz-results-salary');
    var salary = salaryEl ? salaryEl.textContent.replace('Average Salary: ', '') : '';
    var badgeEl = document.getElementById('quiz-results-badge');
    var icon = badgeEl ? badgeEl.textContent : '';
    return { name: name, salary: salary, icon: icon };
  }

  function buildCardHTML(data) {
    var d = document.createElement('div');
    d.style.cssText = 'position:fixed;left:-9999px;top:0;width:' + CARD_W + 'px;height:' + CARD_H + 'px;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;';

    d.innerHTML =
      '<div style="width:' + CARD_W + 'px;height:' + CARD_H + 'px;background:linear-gradient(145deg,#0a0a0a 0%,#1a0f00 35%,#2a1500 65%,#0a0a0a 100%);display:flex;flex-direction:column;justify-content:space-between;padding:52px 60px 44px;box-sizing:border-box;position:relative;">' +

      '<div style="position:absolute;top:0;left:0;width:100%;height:100%;background:radial-gradient(circle at 85% 20%,rgba(255,107,0,0.07) 0%,transparent 50%),radial-gradient(circle at 15% 80%,rgba(255,193,7,0.04) 0%,transparent 40%);pointer-events:none;"></div>' +

      '<div style="position:relative;z-index:1;display:flex;align-items:flex-start;justify-content:space-between;">' +
        '<div style="flex:1;">' +
          '<div style="font-size:5rem;line-height:1;margin-bottom:20px;">' + esc(data.icon || '') + '</div>' +
          '<div style="font-size:1.1rem;font-weight:600;color:#ff6b00;letter-spacing:3px;text-transform:uppercase;margin-bottom:10px;">Your Trade Match</div>' +
          '<div style="font-size:44px;font-weight:900;color:#ffffff;line-height:1.05;margin-bottom:6px;">I\'m built for</div>' +
          '<div style="font-size:56px;font-weight:900;color:#ff6b00;line-height:1.05;margin-bottom:16px;">' + esc(data.name) + '!</div>' +
          '<div style="display:inline-block;padding:8px 22px;background:rgba(255,193,7,0.1);border:1px solid rgba(255,193,7,0.3);border-radius:50px;font-size:1.15rem;font-weight:700;color:#ffc107;">' +
            (data.salary ? 'Average Salary: ' + esc(data.salary) : '') +
          '</div>' +
        '</div>' +
        '<div style="flex-shrink:0;width:180px;height:180px;border-radius:16px;background:rgba(255,107,0,0.08);border:1px solid rgba(255,107,0,0.2);display:flex;align-items:center;justify-content:center;font-size:6rem;align-self:center;">' +
          esc(data.icon || '') +
        '</div>' +
      '</div>' +

      '<div style="position:relative;z-index:1;display:flex;align-items:center;justify-content:space-between;border-top:1px solid #2a2a2a;padding-top:24px;">' +
        '<div style="display:flex;align-items:center;gap:10px;">' +
          '<span style="font-size:1.6rem;">⚒️</span>' +
          '<span style="font-size:1.4rem;font-weight:800;color:#ffffff;">TradeLift</span>' +
        '</div>' +
        '<div style="font-size:0.9rem;color:#8a8a8a;">Take the quiz → https://pablo63leiva-alt.github.io/tradelift/quiz.html</div>' +
      '</div>' +

      '</div>';

    document.body.appendChild(d);
    return d;
  }

  function buildSVGDataUri(cardEl) {
    var svg =
      '<svg xmlns="http://www.w3.org/2000/svg" width="' + CARD_W + '" height="' + CARD_H + '">' +
        '<foreignObject width="100%" height="100%">' +
          '<div xmlns="http://www.w3.org/1999/xhtml" style="width:' + CARD_W + 'px;height:' + CARD_H + 'px;">' +
            cardEl.innerHTML +
          '</div>' +
        '</foreignObject>' +
      '</svg>';
    return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
  }

  function renderToCanvas(cardEl) {
    return new Promise(function (resolve) {
      var canvas = document.createElement('canvas');
      canvas.width = CARD_W;
      canvas.height = CARD_H;
      var img = new Image();
      img.onload = function () {
        var ctx = canvas.getContext('2d');
        if (!ctx) {
          resolve(null);
          return;
        }
        try {
          ctx.drawImage(img, 0, 0, CARD_W, CARD_H);
          resolve(canvas);
        } catch (err) {
          resolve(null);
        }
      };
      img.onerror = function () {
        resolve(null);
      };
      img.src = buildSVGDataUri(cardEl);
    });
  }

  function triggerDownload(canvas, onFail) {
    if (typeof canvas.toBlob !== 'function') {
      if (onFail) onFail();
      return;
    }
    try {
      canvas.toBlob(function (blob) {
        if (!blob) {
          if (onFail) onFail();
          return;
        }
        try {
          var url = URL.createObjectURL(blob);
          var a = document.createElement('a');
          a.href = url;
          a.download = 'tradelift-' + (currentTrade ? currentTrade.name.toLowerCase().replace(/\s+/g, '-') : 'result') + '-card.png';
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
          setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
        } catch (err) {
          if (onFail) onFail();
        }
      }, 'image/png');
    } catch (err) {
      if (onFail) onFail();
    }
  }

  function removeCardEl(cardEl) {
    if (cardEl && cardEl.parentNode) {
      cardEl.parentNode.removeChild(cardEl);
    }
  }

  function showFeedbackFail(svgUri) {
    var btn = downloadBtn || document.getElementById('quiz-download-btn');
    if (btn) {
      btn.disabled = false;
      btn.textContent = "Couldn't generate \u2014 try again";
      setTimeout(function () {
        btn.textContent = DEFAULT_DOWNLOAD_LABEL;
      }, 2000);
    }
    if (svgUri) {
      window.open(svgUri, '_blank');
    }
  }

  function renderScaledFallback(wrapper, cardEl) {
    var containerW = wrapper.clientWidth;
    if (!containerW && previewEl) {
      containerW = previewEl.clientWidth;
    }
    if (!containerW) {
      containerW = CARD_W;
    }
    var scale = containerW / CARD_W;
    var fb = document.createElement('div');
    fb.className = 'quiz-share-preview-fallback';
    fb.style.width = CARD_W + 'px';
    fb.style.height = CARD_H + 'px';
    fb.style.transform = 'scale(' + scale + ')';
    fb.style.transformOrigin = '0 0';
    fb.innerHTML = cardEl.innerHTML;
    wrapper.appendChild(fb);
    wrapper.style.height = Math.round(CARD_H * scale) + 'px';
  }

  function renderPreview(data) {
    if (!previewEl) {
      previewEl = document.getElementById('quiz-share-preview');
    }
    if (!previewEl) return;

    var cardEl = buildCardHTML(data);

    var wrapper = document.createElement('div');
    wrapper.className = 'quiz-share-preview-inner';

    previewEl.innerHTML = '';
    previewEl.appendChild(wrapper);
    previewEl.hidden = false;
    previewEl.removeAttribute('aria-hidden');

    renderToCanvas(cardEl).then(function (canvas) {
      var rendered = false;
      if (canvas) {
        try {
          var img = document.createElement('img');
          img.className = 'quiz-share-preview-img';
          img.alt = 'Your TradeLift result card preview';
          img.src = canvas.toDataURL('image/png');
          wrapper.appendChild(img);
          rendered = true;
        } catch (err) {}
      }
      if (!rendered) {
        renderScaledFallback(wrapper, cardEl);
      }
      removeCardEl(cardEl);
    }).catch(function () {
      renderScaledFallback(wrapper, cardEl);
      removeCardEl(cardEl);
    });
  }

  function handleDownload() {
    if (!currentTrade) return;

    var cardEl = buildCardHTML(currentTrade);
    var svgUri = buildSVGDataUri(cardEl);
    var btn = downloadBtn || document.getElementById('quiz-download-btn');

    function restore() {
      if (btn) {
        btn.disabled = false;
        btn.textContent = DEFAULT_DOWNLOAD_LABEL;
      }
    }

    function fail() {
      removeCardEl(cardEl);
      showFeedbackFail(svgUri);
    }

    if (btn) {
      btn.disabled = true;
      btn.textContent = 'Generating...';
    }

    renderToCanvas(cardEl).then(function (canvas) {
      var failed = false;
      function onFail() {
        failed = true;
        fail();
      }
      if (canvas) {
        triggerDownload(canvas, onFail);
        if (!failed) {
          removeCardEl(cardEl);
          restore();
        }
      } else {
        onFail();
      }
    }).catch(function () {
      fail();
    });
  }

  function initDownloadBtn() {
    downloadBtn = document.getElementById('quiz-download-btn');
    if (downloadBtn) {
      downloadBtn.hidden = false;
      downloadBtn.removeEventListener('click', handleDownload);
      downloadBtn.addEventListener('click', handleDownload);
    }
  }

  function onResultsRevealed() {
    var result = readCurrentResult();
    if (!result) return;
    currentTrade = result;
    initDownloadBtn();
    renderPreview(result);
  }

  document.addEventListener('quiz-results-revealed', onResultsRevealed);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      previewEl = document.getElementById('quiz-share-preview');
    });
  } else {
    previewEl = document.getElementById('quiz-share-preview');
  }
})();
