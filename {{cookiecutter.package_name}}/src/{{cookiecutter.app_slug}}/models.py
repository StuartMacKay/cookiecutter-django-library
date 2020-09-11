{% if cookiecutter.create_copyright_notice == "y" %}
  {%- include "resources/copyright/header.txt" %}
{% endif -%}

from django.db import models
from django.utils.translation import gettext_lazy as _

{% if cookiecutter.create_project == "y" %}
class Example(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=32, blank=True)
{%- endif %}
