PYTHON_INTERPRETER=python3
VENV_PATH=.venv
PYTHON_BIN=$(VENV_PATH)/bin/python
PIP=$(VENV_PATH)/bin/pip
COOKIECUTTER_BIN=$(VENV_PATH)/bin/cookiecutter
SPHINX_RELOAD=$(PYTHON_BIN) sphinx_reload.py

# Formatting variables, FORMATRESET is always to be used last to close formatting
FORMATBLUE:=$(shell tput setab 4)
FORMATBOLD:=$(shell tput bold)
FORMATRESET:=$(shell tput sgr0)

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo
	@echo "  clean                         -- to clean EVERYTHING (Warning)"
	@echo "  clean-pycache                 -- to remove all __pycache__, this is recursive from current directory"
	@echo "  clean-dist                    -- to remove distributed directory"
	@echo "  clean-install                 -- to clean Python side installation"
	@echo "  clean-doc                     -- to remove documentation builds"
	@echo
	@echo "  install                       -- to install this project with virtualenv and Pip"
	@echo
	@echo "  app                           -- to create a new application"
	@echo

clean-pycache:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Clear Python cache <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf .pytest_cache
	find . -type d -name "__pycache__"|xargs rm -Rf
	find . -name "*\.pyc"|xargs rm -f
.PHONY: clean-pycache

clean-dist:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning distributed directory <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf dist
.PHONY: clean-dist

clean-install:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning install <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf $(VENV_PATH)
.PHONY: clean-install

clean: clean-install clean-dist clean-pycache
.PHONY: clean

venv:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Install virtual environment <---$(FORMATRESET)\n"
	@echo ""
	virtualenv -p $(PYTHON_INTERPRETER) $(VENV_PATH)
	# This is required for those ones using old distribution
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade setuptools
.PHONY: venv

install: venv
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Installing requirements <---$(FORMATRESET)\n"
	@echo ""
	$(PIP) install -r requirements/base.txt
	$(PIP) install -r requirements/dev.txt
.PHONY: install

app:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Creating new application <---$(FORMATRESET)\n"
	@echo ""
	@mkdir -p dist
	$(COOKIECUTTER_BIN) -o dist .
.PHONY: app
