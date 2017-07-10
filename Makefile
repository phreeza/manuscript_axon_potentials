.PHONY: refs cleanrefs figs

## Document related stuff
#
#
## Markdown extension (e.g. md, markdown, mdown).
MEXT = md

## All markdown files in the working directory
SRC = $(wildcard doc/*.$(MEXT))

## Location of your working bibliography file
BIB = doc/refs.bib

## CSL stylesheet (located in the csl folder of the PREFIX directory).
CSL = doc/jn

PDFS=$(SRC:.md=.pdf)
TEX=$(SRC:.md=.tex)
FIGS = figs/fig_1.pdf figs/fig_2.pdf figs/fig_3.pdf figs/fig_4.pdf figs/fig_5.pdf


all:	$(PDFS) $(TEX)

pdf:	clean $(PDFS)
tex:	clean $(TEX)


doc/%.tex:	doc/%.md $(BIB) $(FIGS)
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block -w latex -s -S --filter pandoc-crossref --latex-engine=pdflatex --natbib --bibliography=$(BIB) -o $@ $<

doc/%.pdf:	doc/%.md $(BIB) $(FIGS)
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block -s -S --latex-engine=pdflatex  --filter pandoc-crossref --filter pandoc-citeproc --csl=$(CSL).csl --bibliography=$(BIB) -o $@ $<

clean:
	rm -f $(PDFS) $(TEX) $(FIGS)

$(BIB):
	curl "http://www.citeulike.org/bibtex/user/phreeza/tag/axon_lfp_writeup?do_username_prefix=0&key_type=4&incl_amazon=0&clean_urls=1&smart_wrap=0&q=" > $(BIB)

refs:
	curl "http://www.citeulike.org/bibtex/user/phreeza/tag/axon_lfp_writeup?do_username_prefix=0&key_type=4&incl_amazon=0&clean_urls=1&smart_wrap=0&q=" > $(BIB)

cleanrefs:
	rm -f $(BIB)

## Figure related stuff

figs: $(FIGS)

figs/fig_1.pdf: bin/build_fig1.py 
	python bin/build_fig3.py

figs/fig_2.pdf: bin/build_fig2.py
	python bin/build_fig3.py

figs/fig_3.pdf: bin/build_fig3.py
	python bin/build_fig3.py

figs/fig_4.pdf: bin/build_fig4.py
	python bin/build_fig4.py

figs/fig_5.pdf: bin/build_fig5.py
	python bin/build_fig5.py
