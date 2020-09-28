# post_gen_project.py
import os
import shutil
import subprocess


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def git_init():
    # Although there should not be any cruft in the generated project
    # leave adding and committing the files for later. That also neatly
    # sidesteps the issue of setting up or selecting the GPG key if
    # commits are going to be signed.
    subprocess.run(["git", "init"])
    subprocess.run(["git", "remote", "add", "origin", "{{ cookiecutter.repository_url }}"])


create_copyright_notice = "{{ cookiecutter.create_copyright_notice }}" == "y"
create_makefile = "{{ cookiecutter.create_makefile }}" == "y"
create_virtualenv = "{{ cookiecutter.create_virtualenv }}" == "y"
create_project = "{{ cookiecutter.create_project }}" == "y"
create_repository = "{{ cookiecutter.repository_url }}" != ""

use_pytest = "{{ cookiecutter.test_runner}}" == "pytest"
use_readthedocs = "{{ cookiecutter.use_readthedocs}}" == "y"
use_travis = "{{ cookiecutter.continuous_integration }}" == "Travis CI"

if create_virtualenv:
    python = "python{{ cookiecutter.python_version }}"
    pip = "./venv/bin/pip{{ cookiecutter.python_version}}"
    pip_compile = "./venv/bin/pip-compile"
    pip_sync = "./venv/bin/pip-sync"

    subprocess.run([python, "-m", "venv", "venv"])
    subprocess.run([pip, "install", "--upgrade", "pip", "setuptools", "wheel"])
    subprocess.run([pip, "install", "pip-tools"])

    subprocess.run([pip_compile, "requirements/dev.in", "--output-file", "requirements/dev.txt"])
    subprocess.run([pip_compile, "requirements/docs.in", "--output-file", "requirements/docs.txt"])
    subprocess.run([pip_compile, "requirements/tests.in", "--output-file", "requirements/tests.txt"])
    subprocess.run([pip_sync, "requirements/dev.txt"])

# Delete the resources directory tree. It was only used with include
# template directives and it not needed in the generated project.
remove("resources")

if not create_copyright_notice:
    remove("COPYRIGHT.txt")

if not create_makefile:
    remove("Makefile")

if not create_project:
    remove("src/{{ cookiecutter.app_slug }}/locale/en")
    remove("src/{{ cookiecutter.app_slug }}/migrations/0001_initial.py")
    remove("src/{{ cookiecutter.app_slug }}/tests/test_views.py")

if not use_pytest:
    remove("requirements/tests.in")
    remove("requirements/tests.txt")

if not use_readthedocs:
    remove("docs")
    remove("requirements/docs.in")
    remove("requirements/docs.txt")

if not use_readthedocs:
    remove(".readthedocs.yml")

if not use_travis:
    remove(".travis.yml")

if create_repository:
    git_init()

