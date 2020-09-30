# !/usr/bin/env python
import os

from distutils.core import setup


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as fp:
        return fp.read()


setup(
    name="cookiecutter-django-library",
    version="0.2.0",
    description="Cookiecutter template for a installable Django application",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    author="Stuart MacKay",
    license="License :: OSI Approved :: BSD License",
    license_file="LICENSE.txt",
    author_email="smackay@flagstonesoftware.com",
    url="https://github.com/StuartMacKay/cookiecutter-django-library",
    keywords=["cookiecutter", "template", "django", ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework:: Django:: 2.2",
        "Framework:: Django:: 3.0",
        "Framework:: Django:: 3.1",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],
)
