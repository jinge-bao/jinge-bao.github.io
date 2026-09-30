# Jinge Bao's academic website

Website: <https://jinge-bao.github.io/>

Repository: <https://github.com/jinge-bao/jinge-bao.github.io>

Static site built with [jemdoc+MathJax](https://github.com/wsshin/jemdoc_mathjax)
and published on GitHub Pages. Building requires Python 3; the convenience
commands below also use Make. No Python packages need to be installed.

## Edit

Edit the source files, then regenerate the HTML. Do not edit generated HTML
directly: the next build replaces it.

| File | Content |
| --- | --- |
| `index.jemdoc` | Biography, research interests, news and contact details |
| `publications.jemdoc` | Publications and paper links |
| `talks.jemdoc` | Invited talks and conference presentations |
| `teaching.jemdoc` | Teaching and lecture slides |
| `service.jemdoc` | Awards and academic service |
| `cv.jemdoc` and `cv.pdf` | CV page and downloadable CV |
| `MENU` | Navigation, profile links and contact email |
| `mysite.conf` | MathJax configuration |
| `jemdoc.css` | Default jemdoc layout and print styles |
| `photos/profile.jpg` | Profile photograph |
| `slides/` | Downloadable teaching materials |

News lines beginning with `#` are deliberately hidden. Remove the `#` only
when the entry should appear again. Inline math uses `$ ... $`; display math
uses `\( ... \)` in jemdoc source.

## Build and preview

```sh
./build.sh        # rebuild every page
make check        # validate page metadata and local links/resources
make serve        # preview at http://127.0.0.1:8000
```

`make` performs an incremental build and tracks changes to the source files,
menu, configuration and jemdoc generator. The preview server is local to this
computer. Stop it with Ctrl-C.

Keep the six generated HTML files in sync when committing so that opening
the checkout directly also shows the current content.

## Publish

Use **Settings → Pages → Build and deployment → Source: GitHub Actions**.
This repository already has the required workflow; no new workflow is needed.

1. Edit the source, run `./build.sh` and `make check`, and review the result.
2. Commit the source changes and regenerated HTML, then push to `main`.
3. Check **Actions → Build and deploy jemdoc site** for a successful deployment.
4. Visit <https://jinge-bao.github.io/>.

Pull requests build and validate without deploying. On `main`, the workflow
rebuilds from jemdoc, checks local links, and publishes only the generated
pages and public assets. `.nojekyll` keeps GitHub from processing these files
with Jekyll.

### Avoid competing publishers

The workflow checks the actual Pages publishing mode. While Source is still
**Deploy from a branch**, GitHub publishes the committed HTML and this custom
workflow skips its own deployment with a warning. This prevents two different
versions from being published at the same time. In that mode, source-only
edits do not update the website: regenerate and commit the HTML too.
The workflow reports stale committed HTML as an error in this mode, but that
check cannot stop GitHub's separate branch publisher from serving those files.

To enable automatic source builds, change Source to **GitHub Actions**, allow
any previous branch deployment to finish, and run the existing workflow from
the Actions tab (or push the next commit). This setting requires repository
Pages administration access; write access alone may not be enough.

If publishing fails with a permission error, use a GitHub account with write
access to `jinge-bao/jinge-bao.github.io`. The website's linked profile account
and the repository's publishing account need not be the same.
