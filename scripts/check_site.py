#!/usr/bin/env python3
"""Check generated pages and local links without third-party dependencies."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


ROOT = Path(__file__).resolve().parent.parent


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.viewports = []
        self.title = []
        self.in_title = False
        self.errors = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append("duplicate id: " + attrs["id"])
            self.ids.add(attrs["id"])
        if tag == "meta" and attrs.get("name") == "viewport":
            self.viewports.append(attrs.get("content", ""))
        if tag == "title":
            self.in_title = True
        if tag in {"a", "link", "img", "script"}:
            reference = attrs.get("href") or attrs.get("src")
            if reference:
                self.links.append(reference)
        if tag == "img" and "alt" not in attrs:
            self.errors.append("image missing alternative text")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)


def main():
    errors = []
    pages = {}
    for source in sorted(ROOT.glob("*.jemdoc")):
        path = source.with_suffix(".html").resolve()
        if not path.is_file():
            errors.append(f"{path.name}: missing generated page")
        else:
            pages[path] = Page(path)

    if not pages:
        errors.append("no generated pages found")

    references = 0
    for path, page in pages.items():
        errors.extend(f"{path.name}: {error}" for error in page.errors)
        if not "".join(page.title).strip():
            errors.append(f"{path.name}: missing page title")
        if len(page.viewports) != 1 or "width=device-width" not in page.viewports[0]:
            errors.append(f"{path.name}: missing or invalid mobile viewport")

        for reference in page.links:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            references += 1
            if not url.path:
                target = path
            elif url.path.startswith("/"):
                target = ROOT / unquote(url.path).lstrip("/")
            else:
                target = path.parent / unquote(url.path)
            target = target.resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{path.name}: missing local target {reference}")
            elif url.fragment and target in pages:
                if unquote(url.fragment) not in pages[target].ids:
                    errors.append(f"{path.name}: missing fragment {reference}")

    if errors:
        print("Site validation failed:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(pages)} pages and {references} local links/resources.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
