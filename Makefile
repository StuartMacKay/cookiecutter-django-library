#
# Makefile: Commands to simplify development and releases
#
# To avoid having to enter values for all the configuration options each
# time, the cookiecutter command is run the --config-file and --no-input
# options. --no-input just accepts all the defaults from cookiecutter.json.
# These are selectively overridden by the default context in .cookiecutterrc,
# located in the root of the project, with project specific details.

root_dir = $(realpath .)
output_dir := $(realpath ..)

# The generated project can only be done by running the clean-output target
# imported from the clean-output.mk makefile in the generated directory. That
# makes it less likely that you end up deleting more than expected when mucking
# around with this makefile.

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo ""
	@echo "  bake         to run cookiecutter and generate the project"
	@echo

.PHONY: bake
bake:
	cookiecutter . \
	    --config-file .cookiecutterrc \
	    --overwrite-if-exists \
	    --no-input \
	    --output-dir $(output_dir)

# include any local makefiles
-include *.mk
