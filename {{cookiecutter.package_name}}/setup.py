#!/usr/bin/env python
"""
setup.py

setup() is configured with the project metadata so setup.cfg is used
primarily for options for the various tools used.

{# Template code inside the docstring gets removed completely when the project is generated. #}
{%- set license_classifier = {
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "BSD 2-Clause License": "License :: OSI Approved :: BSD License",
    "BSD 3-Clause License": "License :: OSI Approved :: BSD License",
    "GNU General Public License v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "MIT license": "License :: OSI Approved :: MIT License",
    "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
    "Other": "License :: Other/Proprietary License",
}[cookiecutter.project_license] %}
"""
import os

from setuptools import setup


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as fp:
        return fp.read()


setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.project_version }}",
    description="{{ cookiecutter.project_description }}",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    keywords="{{ cookiecutter.project_keywords }}",
{%- if cookiecutter.project_url %}
    url="{{ cookiecutter.project_url }}",
{%- endif %}
    packages=[
        "{{ cookiecutter.app_slug }}",
        "{{ cookiecutter.app_slug }}/migrations"
    ],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires="Django>=2.2",
    license="{{ license_classifier }}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "{{ license_classifier }}",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
