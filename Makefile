DOCS = index publications talks teaching service cv
HTML = $(addsuffix .html, $(DOCS))
CONF = mysite.conf

.PHONY: all check clean serve
all: $(HTML) .nojekyll

%.html: %.jemdoc MENU $(CONF) jemdoc.py
	python3 -W ignore jemdoc.py -o $@ -c $(CONF) $<

.nojekyll:
	touch .nojekyll

check: all
	python3 scripts/check_site.py

serve: all
	python3 -m http.server 8000 --bind 127.0.0.1

clean:
	rm -f $(HTML)
