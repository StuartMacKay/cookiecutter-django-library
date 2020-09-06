{% if cookiecutter.create_copyright_notice == "y" %}
  {%- include "resources/copyright/header.txt" %}
{% endif -%}
from django.contrib import admin

from . import models

{% if cookiecutter.create_project == "y" %}
@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
{%- endif %}
