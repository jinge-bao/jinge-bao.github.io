DOCS = index publications talks teaching service cv
HTML = $(addsuffix .html, $(DOCS))
CONF = mysite.conf

.PHONY: all clean serve
all: $(HTML) .nojekyll

%.html: %.jemdoc MENU $(CONF)
	python3 -W ignore jemdoc.py -o $@ -c $(CONF) $<

.nojekyll:
	touch .nojekyll

serve: all
	python3 -m http.server 8000

clean:
	rm -f $(HTML)
