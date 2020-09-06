cookiecutter-django-library
===========================

A Cookiecutter_ template that contains everything you need to develop a
Django app that can be deployed to PyPI and installed in any project.

You can see what this template generates out of the box at:
https://github.com/StuartMacKay/django-library-project.

Philosophy
----------

This template just adds the basics for an app - a little more than you get
with the startapp management command. Instead the focus on adding all the
infrastructure so everything works out of the box. The goal is to take care
of all the fiddly and time-consuming details that only get done occasionally
but soon add up to real effort.

No cruft - almost all of the features are optional so, if you did not select
it you will not see it in the generated project. That saves you from having
to delete a bunch of stuff you did not want.

Local first - only PyPI for installed dependencies and deploying the project
is considered essential. Integrations with other third-party services are
considered extras and, if included, are optional.

Features
--------

* Build and deploy an app right out of the box.
* Opinionated code formatting with `black`_ and `isort`_.
* Automate tasks for testing, building and deploying your app with `make`_.
* Manage package versions and your virtualenv with `pip-tools`_.
* Make updating version numbers easy with `bump2version`_.
* Sign commits, tags and uploads by default so you don't forget.
* Easily run tests for all supported environments using `tox`_.

Quick start
-----------

Ensure you have cookiecutter installed::

    pip install --user cookiecutter

Then use cookiecutter to generate your project from this template with::

    cookiecutter gh:StuartMacKay/cookiecutter-django-library


Configuration options
---------------------

To generate the project you will be asked for the following fields, in order:

.. list-table::
    :header-rows: 1

    * - Field
      - Default
      - Description

    * - project_name
      - Django App
      - The project's official or human-readable name.

    * - project_description
      - A short description of your project
      - A one line description of what the app does.

    * - project_keywords
      - A list of keywords
      - Metadata (defined in `PEP 0314`_) that can be used to categorize your
        project.

    * - project_version
      - 0.1.0
      - The initial version number of your project. Optionally managed by
        bump2version after that.

    * - project_license
      - Apache Software License 2.0
      - The license to release your project under. The list of choices includes:

           * Apache Software License 2.0
           * BSD 2-Clause License
           * BSD 3-Clause License
           * Common Development and Distribution License
           * GNU General Public License version 3
           * GNU Affero General Public License version 3
           * GNU Lesser General Public License
           * MIT license
           * Mozilla Public License 2.0
           * Other

        There is no preferred license. The Apache Software License 2.0 license
        is the default as it is the first in the list. There are many other
        options available: https://choosealicense.com/.

    * - package_name
      - django_app
      - The name of the distributed package (whatever you would ``pip install``).

    * - python_version
      - 3.8
      - The version of the python interpreter to use. This is used in the
        Makefile when creating the virtualenv for the project.

    * - app_name
      - App
      - The human readable name of the app. Based on ``project_name`` with any
        "Django" prefix removed,

    * - app_slug
      - app
      - The name of the module you would import. Based on the ``app_name``.

    * - app_config
      - AppConfig
      - The name of the Config class used to add the app to the ``INSTALLED_APPS``
        setting. Based on the ``app_name``.

    * - author
      - Author's full name
      - Main author of this App. This can also be the name of an organisation.

    * - author_email
      - Author's email address
      - The email address of the main point of contact for the project. This
        is also used as the point of contact in licenses and copyright notices.

    * - create_copyright_notice
      - y
      - Add a copyright notice, as a header comment, to all source files::

           # Copyright (C) 2020
           # Author: D. Veloper
           # Contact: developer@example.com

        This uses the current year, ``author`` and ``author_email``..

    * - create_makefile
      - y
      - Add a (GNU Make) Makefile to automate project tasks.

    * - create_virtualenv
      - y
      - Create the virtualenv and install the requirements when the project
        is generated.

    * - create_project
      - n
      - Create an example project (views, models, etc.). This is mainly used
        for debugging the template during development.

    * - use_piptools
      - y
      - Use pip-tools for managing dependencies and pinning version numbers.

    * - code_checker
      - flake8
      - Tools for checking code quality. The list of choices includes:

          * `flake8`_
          * `pylama`_
          * other

    * - use_black
      - y
      - Use black for formatting the source files in project.

    * - use_isort
      - y
      - Use isort for organising the import statements in your source files.

    * - use_bumpversion
      - y
      - Use bump2version to managing incrementing the version numbers, found
        in various files, when you do a release.

    * - use_readthedocs
      - y
      - Generate project documentation, using Sphinx, that can be hosted on
        `Read The Docs`_.

    * - use_coverage
      - y
      - Check the quality of your tests using coverage.

    * - sphinx_theme
      - sphinx-rtd-theme
      - The theme to use when generating the docs for Read the Docs. The list
        of choices includes:

          * sphinx-rtd-theme
          * alabaster
          * other

        The theme is only used if ``use_readthedocs`` is set.

    * - sign_commits
      - y
      - Sign commits with a GPG key. Used by bump2version. Read `Signing Your Work`_
        for a good explanation on why you should do it and how.

    * - sign_tags
      - y
      - Sign tags with a GPG key. Used by bump2version.

    * - sign_uploads
      - y
      - Sign uploads to PyPI with a GPG key. Used by twine in the Makefile.

    * - test_runner
      - django
      - The test runner to use. Available options include::

          * django
          * `pytest`_

        Nose has been on maintenance since 2015 so it is not included here.
        There does seem to be a follow-up project, nose2, but it's not clear
        how much life it has right now.


Making a release
----------------
The Makefile is intended to automate as much as possible so releasing a new
patch version is as simple as::

    make patch verify build upload

Alternatively, if you want to release developer releases, bump the version first
then upload whenever you have something new::

    make major

then::

    make test nightly upload

and finally::

    make verify build upload

Even without a Makefile the process is still very simple.

Depending on the scope of the changes, update the package version, for example::

    bump2version minor

Run all the tests::

    tox


Build the release, removing anything leftover previously:

    rm -rf build
    rm -rf src/*.egg-info
    python sdist bdist_wheel

And upload it to PyPI::

    twine upload --skip-existing dist/*


For security, bump2version and twine can sign the packages so your users
know exactly where it came from. You'll need to generate a GPG key first.
`Signing Your Work`_ is a good guide on how to do that.

Changelog
---------

See the `CHANGELOG.rst`_ for a complete history of changes and what is currently
being prepared for release.

Acknowledgements
----------------

The following cookiecutter projects were raided for good ideas:

  * `cookiecutter-django-app-develop <https://github.com/wooyek/cookiecutter-django-app/>`_
  * `cookiecutter-pylibrary <https://github.com/ionelmc/cookiecutter-pylibrary>`_

Both are excellent and it's worth your time to take a look.

.. _black: https://black.readthedocs.io/en/stable/
.. _bump2version: https://github.com/c4urself/bump2version
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _CHANGELOG.rst: https://github.com/StuartMacKay/cookiecutter-django-library/blob/master/CHANGELOG.rst
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://pycqa.github.io/isort/
.. _make: https://www.gnu.org/software/make/manual/html_node/index.html
.. _PEP 0314: https://www.python.org/dev/peps/pep-0314/
.. _pip-tools: https://github.com/jazzband/pip-tools
.. _pylama: https://pylama.readthedocs.io/en/latest/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Read The Docs: https://readthedocs.org/
.. _Signing Your Work: https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work
.. _tox: https://tox.readthedocs.io/en/latest/
