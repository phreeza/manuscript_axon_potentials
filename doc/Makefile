## Put this Makefile in your project directory---i.e., the directory
## containing the paper you are writing. Assuming you are using the
## rest of the toolchain here, you can use it to create .html, .tex,
## and .pdf output files (complete with bibliography, if present) from
## your markdown file. 
## -	Change the paths at the top of the file as needed.
## -	Using `make` without arguments will generate html, tex, and pdf 
## 	output files from all of the files with the designated markdown
##	extension. The default is `.md` but you can change this. 
## -	You can specify an output format with `make tex`, `make pdf` or 
## - 	`make html`. 
## -	Doing `make clean` will remove all the .tex, .html, and .pdf files 
## 	in your working directory. Make sure you do not have files in these
##	formats that you want to keep!

## Markdown extension (e.g. md, markdown, mdown).
MEXT = md

## All markdown files in the working directory
SRC = $(wildcard *.$(MEXT))

## Location of Pandoc support files.
PREFIX = ~/.pandoc

## Location of your working bibliography file
BIB = refs.bib

## CSL stylesheet (located in the csl folder of the PREFIX directory).
CSL = jn


PDFS=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
TEX=$(SRC:.md=.tex)
DOCX=$(SRC:.md=.docx)


all:	$(PDFS) $(HTML) $(TEX) $(DOCX)

pdf:	clean $(PDFS)
html:	clean $(HTML)
tex:	clean $(TEX)
docx:	clean $(DOCX)

%.docx:	%.md
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block -w docx -S --filter pandoc-citeproc --csl=$(CSL).csl --bibliography=$(BIB) -o $@ $<

%.html:	%.md
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block -w html -S  --filter pandoc-citeproc --csl=$(CSL).csl --bibliography=$(BIB) -o $@ $<

%.tex:	%.md
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block -w latex -s -S --latex-engine=pdflatex --filter pandoc-citeproc --csl=$(CSL).csl --bibliography=$(BIB) -o $@ $<


%.pdf:	%.md
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block -s -S --latex-engine=pdflatex --filter pandoc-citeproc --csl=$(CSL).csl --bibliography=$(BIB) -o $@ $<

clean:
	rm -f *.html *.pdf *.tex *.docx

refs:
		curl "http://www.citeulike.org/bibtex/user/phreeza/tag/axon_lfp_writeup?do_username_prefix=0&key_type=4&incl_amazon=0&clean_urls=1&smart_wrap=1&q=" > refs.bib
