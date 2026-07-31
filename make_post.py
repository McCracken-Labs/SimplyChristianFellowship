#!/usr/bin/env python3
"""Generate blog post HTML files from blog/content.json + blog/posts.json.
content.json maps a week number (string) to an object:
  { "lead": str, "verse": str, "ref": str,
    "reflection": [str, ...], "practice": str, "blessing": str,
    "essay": [ {"h2": str-or-empty, "paras": [str, ...]}, ... ] }
Only weeks present in content.json are (re)written. Metadata (title, date,
movement, file) comes from posts.json."""
import json, os, datetime, html

ROOT = os.path.dirname(os.path.abspath(__file__))
posts = {p["week"]: p for p in json.load(open(os.path.join(ROOT, "blog/posts.json")))}
content = json.load(open(os.path.join(ROOT, "blog/content.json")))

def esc(s): return html.escape(s, quote=False)
def fmt(d): return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>(function(){{try{{var t=localStorage.getItem('scf-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
<meta name="theme-color" content="#418892">
<title>{title} | Simply Christian Fellowship</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{base}blog/{file}">
<meta property="og:image" content="{base}assets/logo-full.png">
<meta property="og:site_name" content="Simply Christian Fellowship">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{base}blog/{file}">
<link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32.png">
<link rel="apple-touch-icon" href="../assets/favicon-180.png">
<link rel="alternate" type="application/rss+xml" title="Simply Christian Fellowship" href="../feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/style.css?v=6">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <nav class="nav" aria-label="Primary">
    <a class="brand" href="../index.html" aria-label="Simply Christian Fellowship, home">
      <img class="logo-dark" src="../assets/dove.png" alt="">
      <img class="logo-light" src="../assets/dove-light.png" alt="">
      <span>Simply Christian<small>Fellowship</small></span>
    </a>
    <ul class="nav-links">
      <li><a href="../index.html">Home</a></li>
      <li><a href="../about.html">About</a></li>
      <li><a href="../why.html">Why Simply Christian</a></li>
      <li><a href="../beliefs.html">What We Believe</a></li>
      <li><a href="../science-faith.html">Science &amp; Faith</a></li>
      <li><a href="../practice.html">Ways to Practice</a></li>
      <li><a href="../devotional.html">Devotional</a></li>
      <li><a href="index.html" class="active">Blog</a></li>
    </ul>
    <div class="header-tools">
      <button class="theme-toggle" type="button" aria-label="Toggle dark mode" aria-pressed="false" title="Toggle dark mode">
        <svg class="icon-sun" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
        <svg class="icon-moon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8z"/></svg>
      </button>
      <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </nav>
</header>

<main id="main">
  <article>
'''

FOOT = '''  </article>
</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div>
      <div class="fbrand"><img src="../assets/dove-light.png" alt=""><span>Simply Christian Fellowship</span></div>
      <p>A shared, sincere walk in Christ, free of pressure, with Christ at the center and love as how faith gets lived out.</p>
    </div>
    <nav class="fnav" aria-label="Footer">
      <a href="../index.html">Home</a>
      <a href="../about.html">About</a>
      <a href="../why.html">Why Simply Christian</a>
      <a href="../beliefs.html">What We Believe</a>
      <a href="../science-faith.html">Science &amp; Faith</a>
      <a href="../practice.html">Ways to Practice</a>
      <a href="../devotional.html">Daily Devotional</a>
      <a href="index.html">Sunday Blog</a>
      <a href="../contact.html">Contact &amp; Prayer</a>
    </nav>
  </div>
  <div class="footer-bottom">
    <div class="fb">
      <span>© 2026 Simply Christian Fellowship</span>
      <span>Only Christ is holy.</span>
    </div>
    <p class="site-credit">
      Design &amp; development by
      <a href="https://mccracken-labs.github.io/mccrackenlandservices/labs/" target="_blank" rel="noopener">McCracken Labs</a>
    </p>
  </div>
</footer>

<script src="../assets/site.js?v=6"></script>
<script defer src="../js/count.js" data-endpoint="https://scissortail.mccrackenlabs.workers.dev" data-site="simplychristian"></script>
</body>
</html>
'''

BASE = "https://mccracken-labs.github.io/SimplyChristianFellowship/"

def build(week, c):
    p = posts[int(week)]
    refl = "\n          ".join("<p>%s</p>" % esc(x) for x in c["reflection"])
    essay = []
    for blk in c["essay"]:
        if blk.get("h2"):
            essay.append("        <h2>%s</h2>" % esc(blk["h2"]))
        for para in blk["paras"]:
            essay.append("        <p>%s</p>" % esc(para))
    essay_html = "\n".join(essay)
    head = HEAD.format(title=esc(p["title"]), desc=esc(c["lead"]), base=BASE, file=p["file"])
    body = f'''    <section class="section-tight" style="padding-top:3.2rem;padding-bottom:1rem">
      <div class="wrap post-head">
        <p class="post-meta"><span>Week {p['week']}</span><span class="wk">{esc(p['movement'])}</span><span>{fmt(p['date'])}</span></p>
        <h1 style="color:var(--teal-dark)">{esc(p['title'])}</h1>
        <p class="lead">{esc(c['lead'])}</p>
      </div>
    </section>

    <section class="section-tight" style="padding-top:1rem">
      <div class="wrap">
        <div class="devotional reveal">
          <p class="dev-label">This Week&rsquo;s Devotional</p>
          <p class="dev-ornament">&#10086;</p>
          <p class="dev-open">&ldquo;{esc(c['verse'])}&rdquo;<cite>{esc(c['ref'])}</cite></p>
          <hr class="dev-rule">
          {refl}
          <p class="dev-practice"><b>Practice.</b> {esc(c['practice'])}</p>
          <hr class="dev-rule">
          <p class="dev-bless">{esc(c['blessing'])}</p>
        </div>
      </div>
    </section>

    <section class="section-tight" style="padding-top:0.5rem">
      <div class="wrap post-body article">
{essay_html}
      </div>
    </section>

    <section class="section-tight" style="padding-top:0">
      <div class="wrap">
        <p class="center" style="margin-top:1rem"><a class="btn btn-ghost" href="index.html">&larr; All posts</a></p>
      </div>
    </section>
'''
    open(os.path.join(ROOT, "blog", p["file"]), "w", encoding="utf-8").write(head + body + FOOT)
    return p["file"]

for wk, c in content.items():
    print("wrote", build(wk, c))
