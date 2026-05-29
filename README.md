# Personal Website (jemdoc + MathJax + GitHub Pages)

Static academic homepage built with
[jemdoc+MathJax](https://github.com/wsshin/jemdoc_mathjax).

## Edit

Edit the `*.jemdoc` source files (plain text). Key files:

- `MENU` — sidebar navigation + your name at the top.
- `index.jemdoc` — home / bio. Replace the placeholders and add a `photo.jpg`.
- `research.jemdoc`, `publications.jemdoc`, `teaching.jemdoc`, `group.jemdoc`, `cv.jemdoc`.
- `mysite.conf` — loads MathJax 3 (edit only to change math/analytics).
- `jemdoc.css` — styling.

Math: inline `$ ... $`, display `\( ... \)`. Both are converted and rendered by MathJax.

## Build

```sh
./build.sh          # or:  make
```

Preview locally:

```sh
make serve          # then open http://localhost:8000
```

## Deploy to GitHub Pages

1. Create a repo named **`<username>.github.io`** on GitHub.
2. From this folder:
   ```sh
   git init
   git add .
   git commit -m "Initial website"
   git branch -M main
   git remote add origin https://github.com/<username>/<username>.github.io.git
   git push -u origin main
   ```
3. In the repo: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main` / root.
4. Visit `https://<username>.github.io` (first build takes a minute).

Re-run `./build.sh`, then commit and push to update the live site.
