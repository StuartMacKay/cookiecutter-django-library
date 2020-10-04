#
# Makefile: Commands to simplify development and releases
#
# To avoid having to enter values for all the configuration options each
# time, the cookiecutter command is run the --config-file and --no-input
# options. --no-input just accepts all the defaults from cookiecutter.json.
# These are selectively overridden by the default context in .cookiecutterrc,
# located in the root of the project, with project specific details.

# You can set these variable on the command line.
PYTHON = python3.8

# Where everything lives
site_python := /usr/bin/env $(PYTHON)

root_dir = $(realpath .)
output_dir := $(realpath ..)

python := $(root_dir)/venv/bin/python3
pip := $(root_dir)/venv/bin/pip3
pip-compile := $(root_dir)/venv/bin/pip-compile
pip-sync := $(root_dir)/venv/bin/pip-sync
pytest := $(root_dir)/venv/bin/pytest
bumpversion := $(root_dir)/venv/bin/bump2version

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo ""
	@echo "  clean-tests        to clean the directories created during testing"
	@echo "  clean-venv         to clean the virtualenv"
	@echo "  bake               to run cookiecutter and generate the project"
	@echo "  major              to update the version number for a major release, e.g. 2.1 to 3.0"
	@echo "  minor              to update the version number for a minor release, e.g. 2.1 to 2.2"
	@echo "  patch              to update the version number for a patch release, e.g. 2.1.1 to 2.1.2"
	@echo "  test               to run the tests for all the supported environments"
	@echo "  venv               to create the virtualenv and install dependencies"
	@echo

.PHONY: clean-tests
clean-tests:
	rm -rf .tox
	rm -rf .pytest_cache

.PHONY: clean-venv
clean-venv:
	rm -rf venv

.PHONY: bake
bake:
	cookiecutter . \
	    --config-file .cookiecutterrc \
	    --overwrite-if-exists \
	    --no-input \
	    --output-dir $(output_dir)

.PHONY: major
major:
	$(bumpversion) major

.PHONY: minor
minor:
	$(bumpversion) minor

.PHONY: patch
patch:
	$(bumpversion) patch

.PHONY: test
test: test
	tox

venv:
	$(site_python) -m venv venv
	$(pip) install --upgrade pip setuptools wheel
	$(pip) install pip-tools
	$(pip-sync) -r requirements/dev.txt

# include any local makefiles
-include *.mk
