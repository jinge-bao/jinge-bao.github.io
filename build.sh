#!/usr/bin/env bash
# Build all .jemdoc pages into .html using jemdoc+MathJax.
# Usage: ./build.sh
set -euo pipefail
cd "$(dirname "$0")"

PAGES="index publications talks teaching service cv"
CONF="mysite.conf"

for p in $PAGES; do
  echo "  building $p.html"
  python3 -W ignore jemdoc.py -o "$p.html" -c "$CONF" "$p.jemdoc"
done

# Tell GitHub Pages not to run Jekyll (serve files as-is).
touch .nojekyll
echo "Done. Open index.html in a browser to preview."
