__version__ = "0.0.0"
{%- if cookiecutter.author %}
__author__ = "{{ cookiecutter.author }}"
{%- endif %}
{%- if cookiecutter.author_email %}
__email__ = "{{ cookiecutter.author_email }}"
{%- endif %}
{%- if cookiecutter.project_license != 'Other' %}
__license__ = "{{ cookiecutter.project_license }}"
{%- endif %}
{%- if cookiecutter.create_copyright_notice == "y" %}
__copyright__ = "Copyright (C) {% now 'local', '%Y' %} {{ cookiecutter.author }}"
{%- endif %}
