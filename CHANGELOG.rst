Changelog
=========

Latest
------

* Added cookiecutter parameter for the project's website
* Added cookiecutter parameter for the remote repository URL
* Added .editorconfig
* Added config files for PyCharm
* Added config file for Travis CI
* Added config file for Read the Docs
* Added git repository initialization in the post-generation hook
* Changed the keywords parameter to be a comma-separated list of words
* Changed the requirements so there are separate files for dev, docs and tests
* Changed setup.cfg so tool dependencies use the requirements files
* Changed post-generation hook so creating the virtualenv can be skipped in development
* Changed post-generation hook so initialising the repository can be skipped in development
* Changed the Makefile target, venv, to use the site python version
* Changed the Makefile target, clean, so cleaning the virtualenv is done separately
* Changed the Makefile target, test-all, to test generating the docs
* Removed the cookiecutter parameter, use_piptools, it is needed for managing requirements

v0.1.0 (2020-09-12)
-------------------

* Released first version to PyPI.
