(function () {
  'use strict';

  var TRADES = [
    {
      name: 'Electrician',
      icon: '⚡',
      salary: '$60K – $80K',
      reasons: [
        'You love hands-on work with real systems that power the modern world.',
        'Strong problem-solving skills and attention to detail are your strengths.',
        'Electricians enjoy excellent job security and specialize in a high-demand field.'
      ]
    },
    {
      name: 'Plumber',
      icon: '🔧',
      salary: '$55K – $75K',
      reasons: [
        'You like fixing practical problems that people depend on every day.',
        'You work well independently and don\u2019t mind getting your hands dirty.',
        'Plumbing offers year-round demand and the chance to run your own business.'
      ]
    },
    {
      name: 'Welder',
      icon: '🔥',
      salary: '$45K – $70K',
      reasons: [
        'You thrive in fast-paced, physically active environments.',
        'You enjoy working with your hands to create something visible and lasting.',
        'Welding gets you into the field fast with certification in as little as 6 months.'
      ]
    },
    {
      name: 'HVAC Technician',
      icon: '❄️',
      salary: '$50K – $70K',
      reasons: [
        'You enjoy a mix of indoor precision work and real-world problem solving.',
        'You like working with your hands but also want variety in your day.',
        'HVAC techs stay in demand year-round \u2014 heating in winter, cooling in summer.'
      ]
    },
    {
      name: 'Automotive Mechanic',
      icon: '🚗',
      salary: '$40K – $65K',
      reasons: [
        'You love diagnosing problems and figuring out how things work mechanically.',
        'You prefer hands-on tinkering over sitting at a desk all day.',
        'Auto mechanics can start quickly and even open their own shop someday.'
      ]
    },
    {
      name: 'Carpenter',
      icon: '🪚',
      salary: '$45K – $65K',
      reasons: [
        'You enjoy building things you can see and touch \u2014 real craftsmanship.',
        'Creativity and precision go hand-in-hand for you.',
        'Carpentry is a foundational trade with endless project variety.'
      ]
    },
    {
      name: 'Ironworker',
      icon: '🏗️',
      salary: '$55K – $80K',
      reasons: [
        'You love being outdoors and crave a physically challenging job.',
        'You\u2019re comfortable with heights and high-energy environments.',
        'Ironworkers build iconic structures and earn top-tier pay in the trades.'
      ]
    },
    {
      name: 'Pipefitter',
      icon: '🔩',
      salary: '$60K – $85K',
      reasons: [
        'You enjoy precise, technical work in industrial settings.',
        'You like solving complex system challenges that require careful planning.',
        'Pipefitters are among the highest-paid trades with strong long-term demand.'
      ]
    },
    {
      name: 'Diesel Mechanic',
      icon: '🚛',
      salary: '$45K – $65K',
      reasons: [
        'You love working on big machines and engines that keep the world moving.',
        'Hands-on mechanical problem solving is your zone.',
        'Diesel mechanics enjoy flexible schedules and steady demand in transportation.'
      ]
    },
    {
      name: 'Mason',
      icon: '🧱',
      salary: '$45K – $70K',
      reasons: [
        'You appreciate craftsmanship and take pride in detailed, visible work.',
        'You enjoy building things that last for generations.',
        'Masonry combines physical work with genuine artistry and skill.'
      ]
    },
    {
      name: 'Roofer',
      icon: '🏠',
      salary: '$40K – $65K',
      reasons: [
        'You love being outdoors and don\u2019t mind physical work in all weather.',
        'You like seeing a finished result at the end of every workday.',
        'Roofing is always in demand \u2014 every building needs a roof.'
      ]
    },
    {
      name: 'Construction Manager',
      icon: '📋',
      salary: '$70K – $100K',
      reasons: [
        'You enjoy leading teams and making high-level decisions.',
        'You\u2019re driven by earning potential and career growth.',
        'Starting in the trades and working up to management is a proven path to six figures.'
      ]
    }
  ];

  function tradeSlug(name) {
    return String(name || '').toLowerCase().replace(/\s+/g, '-');
  }

  var TRADE_SLUGS = TRADES.map(function (t) {
    return tradeSlug(t.name);
  });

  var QUESTIONS = [
    {
      q: 'When you picture your ideal workday, what does it look like?',
      options: [
        { text: 'Hands-on with tools, building or fixing something real', scores: { Electrician: 3, Plumber: 2, Carpenter: 2, Welder: 1 } },
        { text: 'Solving a tricky puzzle or diagnosing a hidden problem', scores: { Electrician: 2, 'HVAC Technician': 3, 'Diesel Mechanic': 2, 'Automotive Mechanic': 1 } },
        { text: 'Working with a team on a big, visible project', scores: { Ironworker: 3, 'Construction Manager': 3, Welder: 2, Carpenter: 1 } },
        { text: 'Running my own operation on my own terms', scores: { Plumber: 3, 'Construction Manager': 2, Roofer: 2, Mason: 1 } }
      ]
    },
    {
      q: 'Where do you feel most energized?',
      options: [
        { text: 'Outdoors — fresh air, open sky, moving around', scores: { Ironworker: 3, Roofer: 3, Mason: 2, Plumber: 1 } },
        { text: 'Indoors — controlled environment, focused work', scores: { Electrician: 3, 'HVAC Technician': 3, Carpenter: 2, Pipefitter: 1 } },
        { text: 'Varies — I like switching it up throughout the week', scores: { Plumber: 2, 'HVAC Technician': 2, 'Automotive Mechanic': 3, 'Diesel Mechanic': 1 } },
        { text: 'In a workshop or garage — creative and hands-on', scores: { Welder: 3, Carpenter: 2, Mason: 2, 'Automotive Mechanic': 1 } }
      ]
    },
    {
      q: 'How do you prefer to work?',
      options: [
        { text: 'Solo — I focus best with headphones on and no distractions', scores: { Welder: 3, Plumber: 2, Electrician: 2, 'Diesel Mechanic': 1 } },
        { text: 'With a partner or small crew — collaboration makes it fun', scores: { Ironworker: 2, Carpenter: 3, Mason: 2, Welder: 1 } },
        { text: 'Leading a team — I naturally step up to coordinate', scores: { 'Construction Manager': 3, Pipefitter: 2, Electrician: 1, Ironworker: 1 } },
        { text: 'Doesn\u2019t matter — I can adapt to any work dynamic', scores: { 'HVAC Technician': 2, Plumber: 2, 'Automotive Mechanic': 2, 'Construction Manager': 2 } }
      ]
    },
    {
      q: 'When something breaks, your first instinct is to:',
      options: [
        { text: 'Figure out the root cause before touching anything', scores: { Electrician: 3, Pipefitter: 3, 'HVAC Technician': 2, 'Diesel Mechanic': 1 } },
        { text: 'Dive in and start hands-on troubleshooting', scores: { 'Automotive Mechanic': 3, 'Diesel Mechanic': 3, Plumber: 2, Welder: 1 } },
        { text: 'Ask what happened and work backward logically', scores: { 'Construction Manager': 3, Electrician: 2, Pipefitter: 1, 'HVAC Technician': 1 } },
        { text: 'Adapt and improvise a solution on the spot', scores: { Welder: 3, Roofer: 2, Mason: 2, Carpenter: 1 } }
      ]
    },
    {
      q: 'How important is physical activity in your work?',
      options: [
        { text: 'Very — I want to feel physically tired at the end of the day', scores: { Ironworker: 3, Roofer: 3, Welder: 2, Mason: 1 } },
        { text: 'Moderate — a mix of movement and focused sitting/standing', scores: { Electrician: 2, 'HVAC Technician': 3, Plumber: 2, Pipefitter: 1 } },
        { text: 'Some — I like physical work but don\u2019t want to be exhausted', scores: { Carpenter: 3, Mason: 2, 'Automotive Mechanic': 2, 'Diesel Mechanic': 1 } },
        { text: 'Minimal — I\u2019d rather focus on the mind and hands', scores: { 'Construction Manager': 3, Electrician: 2, Pipefitter: 2, 'HVAC Technician': 1 } }
      ]
    },
    {
      q: 'Which of these sounds most like you?',
      options: [
        { text: 'I like building or creating things with my hands', scores: { Carpenter: 3, Mason: 3, Roofer: 2, Welder: 1 } },
        { text: 'I like understanding how systems and machines work', scores: { Electrician: 3, 'HVAC Technician': 3, Pipefitter: 2, 'Automotive Mechanic': 1 } },
        { text: 'I like organizing people and projects to get results', scores: { 'Construction Manager': 3, Pipefitter: 2, Ironworker: 1, Electrician: 1 } },
        { text: 'I like solving immediate, practical problems', scores: { Plumber: 3, 'Automotive Mechanic': 2, 'Diesel Mechanic': 2, Roofer: 1 } }
      ]
    },
    {
      q: 'What matters most to you in a career?',
      options: [
        { text: 'Making good money without four years of college', scores: { Pipefitter: 3, 'Construction Manager': 2, Electrician: 2, Plumber: 1 } },
        { text: 'Job security \u2014 work that\u2019s always in demand', scores: { Electrician: 3, Plumber: 3, 'HVAC Technician': 2, Roofer: 1 } },
        { text: 'Freedom to work independently or start my own business', scores: { Plumber: 3, Roofer: 2, Carpenter: 2, 'Automotive Mechanic': 1 } },
        { text: 'Variety \u2014 different projects, different challenges', scores: { 'HVAC Technician': 3, 'Automotive Mechanic': 2, Welder: 2, Mason: 1 } }
      ]
    },
    {
      q: 'How do you feel about taking risks on the job?',
      options: [
        { text: 'Bring it on \u2014 I thrive on adrenaline and challenge', scores: { Ironworker: 3, Roofer: 3, Welder: 2, 'Construction Manager': 1 } },
        { text: 'Calculated risks are fine when the safety plan is solid', scores: { Electrician: 2, Plumber: 2, 'HVAC Technician': 3, Pipefitter: 1 } },
        { text: 'I prefer a steady, predictable work environment', scores: { Carpenter: 3, Mason: 3, 'Diesel Mechanic': 2, 'Construction Manager': 1 } },
        { text: 'I\u2019m focused on the end result, not the risk', scores: { 'Construction Manager': 3, Pipefitter: 2, Electrician: 1, Plumber: 1 } }
      ]
    },
    {
      q: 'How do you learn best?',
      options: [
        { text: 'Watching someone do it, then trying it myself', scores: { Welder: 3, Carpenter: 3, Mason: 2, Roofer: 1 } },
        { text: 'Step-by-step instructions I can follow and practice', scores: { Electrician: 3, 'HVAC Technician': 3, Plumber: 2, Pipefitter: 1 } },
        { text: 'Jumping in and figuring it out by doing', scores: { 'Automotive Mechanic': 3, 'Diesel Mechanic': 3, Welder: 2, Roofer: 1 } },
        { text: 'Studying the systems behind how things work', scores: { Pipefitter: 3, Electrician: 2, 'Construction Manager': 2, 'HVAC Technician': 1 } }
      ]
    },
    {
      q: 'How do you think about work-life balance?',
      options: [
        { text: 'I want steady hours and weekends off', scores: { Electrician: 3, 'HVAC Technician': 2, Carpenter: 2, 'Diesel Mechanic': 1 } },
        { text: 'I don\u2019t mind overtime if the pay is worth it', scores: { Ironworker: 3, Pipefitter: 3, Welder: 2, 'Construction Manager': 1 } },
        { text: 'I want to build toward owning my own business', scores: { Plumber: 3, 'Construction Manager': 2, Roofer: 2, 'Automotive Mechanic': 1 } },
        { text: 'Flexible hours matter more than a set schedule', scores: { 'Diesel Mechanic': 3, Welder: 2, 'Automotive Mechanic': 2, Mason: 1 } }
      ]
    }
  ];

  var currentQuestion = 0;
  var scores = {};
  var locked = false;
  var emailSubmitted = false;
  var QUIZ_EMAIL_CONFIG = {
    formspreeEndpoint: 'https://formspree.io/f/xzebljww'
  };
  var questionArea;
  var resultsArea;
  var progressFill;
  var progressText;
  var questionEl;
  var optionsEl;

  function init() {
    questionArea = document.getElementById('quiz-question-area');
    resultsArea = document.getElementById('quiz-results');
    progressFill = document.getElementById('quiz-progress-fill');
    progressText = document.getElementById('quiz-progress-text');
    questionEl = document.getElementById('quiz-question');
    optionsEl = document.getElementById('quiz-options');

    if (!questionArea || !resultsArea || !progressFill) {
      return;
    }

    TRADES.forEach(function (t) {
      scores[t.name] = 0;
    });

    var retakeBtn = document.getElementById('quiz-retake-btn');
    if (retakeBtn) {
      retakeBtn.addEventListener('click', retake);
    }

    var shareBtn = document.getElementById('quiz-share-btn');
    if (shareBtn) {
      shareBtn.addEventListener('click', share);
    }

    var skipBtn = document.getElementById('quiz-email-skip');
    if (skipBtn) {
      skipBtn.addEventListener('click', function () {
        document.getElementById('quiz-email-capture').hidden = true;
      });
    }

    var emailForm = document.getElementById('quiz-email-form');
    if (emailForm) {
      emailForm.addEventListener('submit', handleEmailSubmit);
    }

    renderQuestion();
  }

  function renderQuestion() {
    locked = false;
    var q = QUESTIONS[currentQuestion];
    var total = QUESTIONS.length;
    var num = currentQuestion + 1;
    var pct = (num / total) * 100;

    progressFill.style.width = pct + '%';
    progressText.textContent = 'Question ' + num + ' of ' + total;
    questionEl.textContent = q.q;

    optionsEl.innerHTML = '';
    optionsEl.setAttribute('role', 'radiogroup');
    optionsEl.setAttribute('aria-labelledby', 'quiz-question');
    var letters = ['A', 'B', 'C', 'D'];

    q.options.forEach(function (opt, i) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'quiz-option';
      btn.setAttribute('role', 'radio');
      btn.setAttribute('aria-checked', 'false');

      var letterSpan = document.createElement('span');
      letterSpan.className = 'quiz-option-letter';
      letterSpan.textContent = letters[i];

      var textSpan = document.createElement('span');
      textSpan.textContent = opt.text;

      btn.appendChild(letterSpan);
      btn.appendChild(textSpan);

      btn.addEventListener('click', function () {
        selectOption(i);
      });

      optionsEl.appendChild(btn);
    });

    questionArea.hidden = false;
    resultsArea.hidden = true;

    questionArea.style.animation = 'none';
    void questionArea.offsetHeight;
    questionArea.style.animation = '';
  }

  function selectOption(index) {
    if (locked) return;
    locked = true;

    var btns = optionsEl.querySelectorAll('.quiz-option');
    btns.forEach(function (btn, i) {
      btn.classList.toggle('selected', i === index);
      btn.setAttribute('aria-checked', i === index ? 'true' : 'false');
    });

    var clickedBtn = btns[index];
    if (clickedBtn) {
      clickedBtn.disabled = true;
      clickedBtn.blur();
    }

    var opt = QUESTIONS[currentQuestion].options[index];
    Object.keys(opt.scores).forEach(function (trade) {
      if (scores[trade] !== undefined) {
        scores[trade] += opt.scores[trade];
      }
    });

    setTimeout(function () {
      currentQuestion++;
      if (currentQuestion < QUESTIONS.length) {
        renderQuestion();
      } else {
        showResults();
      }
    }, 280);
  }

  function showResults() {
    var winner = TRADES[0];
    var maxScore = 0;

    TRADES.forEach(function (trade) {
      if (scores[trade.name] > maxScore) {
        maxScore = scores[trade.name];
        winner = trade;
      }
    });

    var badge = document.getElementById('quiz-results-badge');
    var tradeEl = document.getElementById('quiz-results-trade');
    var salaryEl = document.getElementById('quiz-results-salary');
    var reasonsEl = document.getElementById('quiz-results-reasons');

    if (badge) badge.textContent = winner.icon;
    if (tradeEl) {
      tradeEl.textContent = 'You\u2019re built for ' + winner.name + '!';
      tradeEl.setAttribute('data-trade', winner.name);
    }
    if (salaryEl) salaryEl.textContent = 'Average Salary: ' + winner.salary;

    if (reasonsEl) {
      reasonsEl.innerHTML = '';
      winner.reasons.forEach(function (reason) {
        var li = document.createElement('li');
        li.textContent = reason;
        reasonsEl.appendChild(li);
      });
    }

    questionArea.hidden = true;
    resultsArea.hidden = false;

    progressFill.style.width = '100%';
    progressText.textContent = 'Quiz complete!';

    var emailTradeName = document.getElementById('quiz-email-trade-name');
    if (emailTradeName) emailTradeName.textContent = winner.name;
    var emailCapture = document.getElementById('quiz-email-capture');
    if (emailCapture) {
      resetEmailCapture();
      emailCapture.hidden = false;
    }

    document.dispatchEvent(new Event('quiz-results-revealed'));

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function retake() {
    currentQuestion = 0;
    TRADES.forEach(function (t) {
      scores[t.name] = 0;
    });
    resetEmailCapture();
    renderQuestion();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function trackCapture(trade, mode) {
    var entry = { trade: trade, ts: Date.now() };
    if (mode) entry.mode = mode;
    document.dispatchEvent(new CustomEvent('quiz-email-captured', { detail: entry }));
    try {
      var key = 'tradelift_capture_events';
      var list = [];
      try {
        list = JSON.parse(localStorage.getItem(key) || '[]') || [];
      } catch (err) {
        list = [];
      }
      if (!Array.isArray(list)) list = [];
      list.push(entry);
      localStorage.setItem(key, JSON.stringify(list.slice(-50)));
    } catch (err) {}
  }

  function handleEmailSubmit(e) {
    e.preventDefault();
    var submitBtn = document.getElementById('quiz-email-submit');
    if (emailSubmitted || (submitBtn && submitBtn.disabled)) return;
    var honeypot = document.querySelector('#quiz-email-form [name="_gotcha"]');
    if (honeypot && honeypot.value) return;

    var emailInput = document.getElementById('quiz-email-input');
    var emailError = document.getElementById('quiz-email-error');
    var email = emailInput ? emailInput.value.trim() : '';
    var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!email || !pattern.test(email)) {
      if (emailError) emailError.textContent = 'Please enter a valid email address.';
      return;
    }

    if (emailError) emailError.textContent = '';
    if (!submitBtn) return;

    var originalText = submitBtn.textContent;
    var tradeName = getTradeName();

    if (QUIZ_EMAIL_CONFIG.formspreeEndpoint.indexOf('YOURID') !== -1) {
      trackCapture(tradeName, 'mailto');
      window.location.href = 'mailto:?subject=' + encodeURIComponent(tradeName + ' Career Roadmap Request') + '&body=' + encodeURIComponent('Send me the free ' + tradeName + ' Career Roadmap. Email: ' + email);
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
      return;
    }

    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;

    fetch(QUIZ_EMAIL_CONFIG.formspreeEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email, trade: tradeName })
    })
      .then(function (res) {
        if (!res.ok) {
          throw new Error('Formspree ' + res.status);
        }
        return res;
      })
      .then(function () {
        emailSubmitted = true;
        trackCapture(tradeName);
        var form = document.getElementById('quiz-email-form');
        if (form) form.hidden = true;
        var successTrade = document.getElementById('quiz-email-success-trade');
        if (successTrade) successTrade.textContent = tradeName;
        showRoadmapDownload(tradeName);
        var successEl = document.getElementById('quiz-email-success');
        if (successEl) successEl.hidden = false;
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
      })
      .catch(function () {
        trackCapture(tradeName, 'mailto');
        window.location.href = 'mailto:?subject=' + encodeURIComponent(tradeName + ' Career Roadmap Request') + '&body=' + encodeURIComponent('Send me the free ' + tradeName + ' Career Roadmap. Email: ' + email);
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
      });
  }

  function resetEmailCapture() {
    emailSubmitted = false;
    var capture = document.getElementById('quiz-email-capture');
    if (capture) capture.hidden = true;
    var form = document.getElementById('quiz-email-form');
    if (form) {
      form.hidden = false;
      form.reset();
    }
    var success = document.getElementById('quiz-email-success');
    if (success) success.hidden = true;
    var roadmapCta = document.getElementById('quiz-email-roadmap-cta');
    if (roadmapCta) roadmapCta.hidden = true;
    var roadmapLink = document.getElementById('quiz-email-roadmap-link');
    if (roadmapLink) {
      roadmapLink.href = '#';
      roadmapLink.removeAttribute('download');
    }
    var error = document.getElementById('quiz-email-error');
    if (error) error.textContent = '';
    var submitBtn = document.getElementById('quiz-email-submit');
    if (submitBtn) {
      submitBtn.textContent = 'Send Me the Roadmap';
      submitBtn.disabled = false;
    }
  }

  function getTradeName() {
    var tradeEl = document.getElementById('quiz-results-trade');
    if (!tradeEl) return '';
    return tradeEl.getAttribute('data-trade') || tradeEl.textContent.replace('You\u2019re built for ', '').replace('!', '');
  }

  function showRoadmapDownload(tradeName) {
    var cta = document.getElementById('quiz-email-roadmap-cta');
    var link = document.getElementById('quiz-email-roadmap-link');
    if (!cta || !link) return;
    var slug = tradeSlug(tradeName);
    if (TRADE_SLUGS.indexOf(slug) === -1) return;
    fetch('assets/roadmaps/' + slug + '-roadmap', { method: 'HEAD' })
      .then(function (res) {
        if (res.ok) {
          link.href = 'assets/roadmaps/' + slug + '-roadmap';
          link.setAttribute('download', slug + '-roadmap.pdf');
          link.textContent = 'Download your free ' + tradeName + ' Roadmap';
          cta.hidden = false;
        }
      })
      .catch(function () {});
  }

  function share() {
    var tradeEl = document.getElementById('quiz-results-trade');
    if (!tradeEl) return;

    var tradeName = tradeEl.getAttribute('data-trade') || tradeEl.textContent.replace('You\u2019re built for ', '').replace('!', '');
    var text = 'I\u2019m built for ' + tradeName + '! Take the TradeLift quiz: https://tradelift.surge.sh/quiz.html';

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        showShareFeedback();
      }).catch(function () {
        fallbackCopy(text);
      });
    } else {
      fallbackCopy(text);
    }
  }

  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand('copy');
      showShareFeedback();
    } catch (e) {
    }
    document.body.removeChild(ta);
  }

  function showShareFeedback() {
    var btn = document.getElementById('quiz-share-btn');
    if (!btn) return;
    var original = btn.textContent;
    btn.textContent = 'Copied to clipboard!';
    btn.disabled = true;
    setTimeout(function () {
      btn.textContent = original;
      btn.disabled = false;
    }, 2000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();