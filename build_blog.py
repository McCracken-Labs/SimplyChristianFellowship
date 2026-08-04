#!/usr/bin/env python3
"""Regenerate blog/index.html (archive) and feed.xml from blog/posts.json.
A post is published when its file exists AND (its date has arrived OR it is the
launch post, week 1). Future Sunday posts stay hidden until their date. Run on a
weekly schedule by .github/workflows/publish.yml so each week's post goes live
and enters the RSS feed automatically."""
import json, os, datetime, html

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://mccracken-labs.github.io/SimplyChristianFellowship/"
posts = json.load(open(os.path.join(ROOT, "blog/posts.json")))
today = datetime.date.today()

def is_published(p):
    fp = os.path.join(ROOT, "blog", p["file"])
    if not os.path.exists(fp):
        return False
    d = datetime.date.fromisoformat(p["date"])
    return p.get("week") == 1 or d <= today

pub = [p for p in posts if is_published(p)]
pub.sort(key=lambda p: p["date"], reverse=True)

def fmt(d):
    return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")

# ---------- archive list markup ----------
items = []
for p in pub:
    items.append(f'''        <a class="post-item reveal" href="{html.escape(p['file'])}">
          <p class="post-meta"><span>Week {p['week']}</span><span class="wk">{html.escape(p['movement'])}</span><span>{fmt(p['date'])}</span></p>
          <h3>{html.escape(p['title'])}</h3>
          <p>{html.escape(p['summary'])}</p>
        </a>''')
list_html = "\n".join(items) if items else '<p class="center">The first devotional is on its way. Check back soon.</p>'

NAV = '''    <ul class="nav-links">
      <li><a href="../index.html">Home</a></li>
      <li><a href="../about.html">About</a></li>
      <li><a href="../why.html">Why Simply Christian</a></li>
      <li><a href="../beliefs.html">What We Believe</a></li>
      <li><a href="../science-faith.html">Science &amp; Faith</a></li>
      <li><a href="../practice.html">Ways to Practice</a></li>
      <li><a href="../devotional.html">Devotional</a></li>
      <li><a href="index.html" class="active">Blog</a></li>
    </ul>'''

TOOLS = '''    <div class="header-tools">
      <button class="theme-toggle" type="button" aria-label="Toggle dark mode" aria-pressed="false" title="Toggle dark mode">
        <svg class="icon-sun" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
        <svg class="icon-moon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8z"/></svg>
      </button>
      <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>'''

SIGNUP = '''      <div class="signup">
        <h3>Follow the Sunday reflections</h3>
        <p>A new reflection each Sunday, always free. Follow the feed in any reader and each one comes to you, at no cost.</p>
        <p style="margin:0"><a class="btn btn-ghost" href="../feed.xml">Subscribe by RSS</a></p>
        <details class="rss-help">
          <summary>New to RSS? Here is how to follow along</summary>
          <div class="rss-body">
            <p>RSS is a free way to get new posts automatically, with no account to create if you would rather not. Pick whichever way feels easier.</p>
            <p><b>Get new posts by email.</b> Open a free service such as Blogtrottr or follow.it, paste the feed address below, and enter your email. Each new Sunday reflection then arrives in your inbox on its own. Nothing to install.</p>
            <p><b>Use a reader app.</b> Install a free app such as Feedly or Inoreader, tap Add feed or Subscribe, and paste the same address. New posts gather there for whenever you want them.</p>
            <p><b>The feed address to paste</b><br><code>https://mccracken-labs.github.io/SimplyChristianFellowship/feed.xml</code></p>
            <p>The daily devotional has its own page that changes every day. The easiest way to follow it is to bookmark the <a href="../devotional.html">Daily Devotional</a> page and open it each morning.</p>
          </div>
        </details>
      </div>'''

archive = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>(function(){{try{{var t=localStorage.getItem('scf-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
<meta name="theme-color" content="#418892">
<title>Blog &amp; Devotional | Simply Christian Fellowship</title>
<meta name="description" content="A weekly devotional and reflection walking through the teachings of Jesus. A new entry each Sunday.">
<meta property="og:type" content="website">
<meta property="og:title" content="Blog &amp; Devotional | Simply Christian Fellowship">
<meta property="og:description" content="A weekly devotional and reflection walking through the teachings of Jesus. A new entry each Sunday.">
<meta property="og:url" content="{BASE}blog/">
<meta property="og:image" content="{BASE}assets/logo-full.png">
<meta property="og:site_name" content="Simply Christian Fellowship">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{BASE}blog/">
<link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32.png">
<link rel="apple-touch-icon" href="../assets/favicon-180.png">
<link rel="alternate" type="application/rss+xml" title="Simply Christian Fellowship" href="../feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/style.css?v=7">
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
{NAV}
{TOOLS}
  </nav>
</header>

<main id="main">
  <section class="section-tight" style="padding-top:3.5rem">
    <div class="wrap read center">
      <p class="eyebrow">Blog &amp; Devotional</p>
      <h1 style="color:var(--teal-dark)">A word for each week</h1>
      <p class="lead">A short devotional and a longer reflection, walking slowly through the teachings of Jesus. A new entry each Sunday.</p>
    </div>
  </section>

  <section class="section-tight" style="padding-top:0.5rem">
    <div class="wrap">
      <div class="post-list">
{list_html}
      </div>
    </div>
  </section>

  <section class="section-tight" style="padding-top:0">
    <div class="wrap">
{SIGNUP}
    </div>
  </section>
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

<script src="../assets/site.js?v=7"></script>
<script defer src="../js/count.js" data-endpoint="https://scissortail.mccrackenlabs.workers.dev" data-site="simplychristian"></script>
</body>
</html>
'''
open(os.path.join(ROOT, "blog/index.html"), "w", encoding="utf-8").write(archive)

# ---------- RSS feed ----------
def rfc822(d):
    dt = datetime.datetime.fromisoformat(d + "T12:00:00+00:00")
    return dt.strftime("%a, %d %b %Y %H:%M:%S +0000")

rss_items = []
for p in pub:
    link = BASE + "blog/" + p["file"]
    rss_items.append(f'''    <item>
      <title>{html.escape(p['title'])}</title>
      <link>{link}</link>
      <guid isPermaLink="true">{link}</guid>
      <pubDate>{rfc822(p['date'])}</pubDate>
      <description>{html.escape(p['summary'])}</description>
    </item>''')

feed = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Simply Christian Fellowship</title>
    <link>{BASE}blog/</link>
    <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="{BASE}feed.xml" rel="self" type="application/rss+xml"/>
    <description>A weekly devotional and reflection walking through the teachings of Jesus.</description>
    <language>en-us</language>
{chr(10).join(rss_items)}
  </channel>
</rss>
'''
open(os.path.join(ROOT, "feed.xml"), "w", encoding="utf-8").write(feed)

print(f"Published {len(pub)} of {len(posts)} posts. Wrote blog/index.html and feed.xml.")
