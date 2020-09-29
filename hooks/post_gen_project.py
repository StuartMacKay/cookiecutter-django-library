# post_gen_project.py
import os
import shutil
import subprocess

COOKIECUTTER_ENV = os.environ.get("COOKIECUTTER_ENV")

CREATE_COPYRIGHT_NOTICE = "{{ cookiecutter.create_copyright_notice }}" == "y"
CREATE_MAKEFILE = "{{ cookiecutter.create_makefile }}" == "y"
CREATE_VIRTUALENV = "{{ cookiecutter.create_virtualenv }}" == "y"
CREATE_PROJECT = "{{ cookiecutter.create_project }}" == "y"
CREATE_REPOSITORY = "{{ cookiecutter.repository_url }}" != ""

USE_PYTEST = "{{ cookiecutter.test_runner}}" == "pytest"
USE_READTHEDOCS = "{{ cookiecutter.use_readthedocs}}" == "y"
USE_TRAVIS = "{{ cookiecutter.continuous_integration }}" == "Travis CI"

if COOKIECUTTER_ENV == 'dev':
    CREATE_VIRTUALENV = not os.path.exists("venv")
    CREATE_REPOSITORY = not os.path.exists(".git")


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def create_venv():
    python = "python{{ cookiecutter.python_version }}"
    pip = "./venv/bin/pip{{ cookiecutter.python_version }}"
    pip_compile = "./venv/bin/pip-compile"
    pip_sync = "./venv/bin/pip-sync"

    subprocess.run([python, "-m", "venv", "venv"])
    subprocess.run([pip, "install", "--upgrade", "pip", "setuptools", "wheel"])
    subprocess.run([pip, "install", "pip-tools"])

    subprocess.run([pip_compile, "requirements/dev.in", "--output-file", "requirements/dev.txt"])
    subprocess.run([pip_compile, "requirements/docs.in", "--output-file", "requirements/docs.txt"])
    subprocess.run([pip_compile, "requirements/tests.in", "--output-file", "requirements/tests.txt"])
    subprocess.run([pip_sync, "requirements/dev.txt"])


def cleanup():
    # Delete the resources directory tree. It was only used with include
    # template directives and it not needed in the generated project.
    remove("resources")

    if not CREATE_COPYRIGHT_NOTICE:
        remove("COPYRIGHT.txt")

    if not CREATE_MAKEFILE:
        remove("Makefile")

    if not CREATE_PROJECT:
        remove("src/{{ cookiecutter.app_slug }}/locale/en")
        remove("src/{{ cookiecutter.app_slug }}/migrations/0001_initial.py")
        remove("src/{{ cookiecutter.app_slug }}/tests/test_views.py")

    if not USE_PYTEST:
        remove("requirements/tests.in")
        remove("requirements/tests.txt")

    if not USE_READTHEDOCS:
        remove("docs")
        remove("requirements/docs.in")
        remove("requirements/docs.txt")
        remove(".readthedocs.yml")

    if not USE_TRAVIS:
        remove(".travis.yml")


def git_init():
    # Although there should not be any cruft in the generated project
    # leave adding and committing the files for later. That also neatly
    # sidesteps the issue of setting up or selecting the GPG key if
    # commits are going to be signed.
    subprocess.run(["git", "init"])
    subprocess.run(["git", "remote", "add", "origin", "{{ cookiecutter.repository_url }}"])


if __name__ == '__main__':

    if CREATE_VIRTUALENV:
        create_venv()

    if CREATE_REPOSITORY:
        git_init()

    cleanup()
