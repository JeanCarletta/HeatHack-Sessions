# Makefile for HeatHack learning materials.
#
#


# Structure
BOOK_CONFIG = _config.yml
BOOK_TOC = _toc.yml


# ----- Tools -----


# Base commands                   
JUPYTER_BOOK = jupyter-book
CP = cp
CHDIR = cd
RM = rm -rf # on powershell, Remove-Item -Recurse -Force 
ECHO = echo
MV = mv

# Root directory
ROOT = $(shell pwd)

# Jupyter Book construction
OUT_DIR = docs

# ----- Top-level targets -----

# Default prints a help message
help:
	@make usage

# Build HTML - what am I doing about the overall introduction (in front-matter?) - just telling people
# to read it before session1, I guess.
# Maybe I should build these all in one "book", but then something said I can't get
# each chapter starting on a new page and better to need to staple the pdfs.
  
.PHONY: front-matter session1 session2 session3 session4 facilitator-guide technology-guide

front-matter session1 session2 session3 session4 facilitator-guide technology-guide: 
	$(JUPYTER_BOOK) build $@
	$(MV) $@/_build ./$(OUT_DIR)/$@

sessions: front-matter session1 session2 session3 session4

guides: facilitator-guide technology-guide

html: sessions guides

# Clean up the build

clean:
	$(RM) */_build

reallyclean: clean
	$(RM) $(OUT_DIR)/*


# ----- Usage -----

define HELP_MESSAGE

Production:
	make sessions     make the HTML for the four sessions
	make guides       make the HTML for the special guides
	make session1     make HTML for the named session
	make session2     make HTML for the named session
	make session3     make HTML for the named session
	make session4     make HTML for the named session
	make html         make all the HTML outputs

Maintenance:
	make clean        rm the built files from their temporary locations
	make reallyclean  rm the built files including from their served locations

endef
export HELP_MESSAGE

## doesn't work
usage:
	@echo "$$HELP_MESSAGE"
