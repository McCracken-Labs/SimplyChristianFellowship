# Simply Christian Fellowship — Website

A calm, static website for Simply Christian Fellowship. No build step, no
frameworks, no database — just HTML and CSS you can open, edit, and host
anywhere.

## Pages
- `index.html` — Home
- `about.html` — About Us + Fellowship Unifies
- `why.html` — Why Simply Christian?
- `beliefs.html` — What We Believe (Only Christ Is Holy, No Tithing Required, Following Christ Through Action, No Infallible Human Intermediaries)
- `science-faith.html` — Science & Faith
- `practice.html` — Ways to Practice
- `assets/` — logo, dove mark, favicons, stylesheet, and one small script

## Editing the words
All text lives directly in the `.html` files. Open any file in a text
editor, change the words between the tags, and save. The styling is all in
`assets/style.css` — the brand teal is `#418892` if you ever want to adjust it.

## Hosting on GitHub Pages (free)
1. Create a free account at github.com if you don't have one.
2. Make a new **public** repository. For a personal site, name it
   `yourusername.github.io`; otherwise any name works.
3. Upload every file in this folder (keep the `assets` folder intact) — you
   can drag-and-drop them on the repo's "Add file → Upload files" page.
4. Go to the repo's **Settings → Pages**. Under "Build and deployment",
   set **Source: Deploy from a branch**, **Branch: main**, **Folder: / (root)**,
   then Save.
5. Wait about a minute, then visit your site:
   - `https://yourusername.github.io` (if you named the repo that), or
   - `https://yourusername.github.io/repo-name/` (for any other name).

The `.nojekyll` file in this folder tells GitHub to serve the files as-is.

## Later: your own domain
In Settings → Pages you can add a custom domain (like
`simplychristianfellowship.org`) once you buy one, and GitHub will host it
for free with HTTPS.
