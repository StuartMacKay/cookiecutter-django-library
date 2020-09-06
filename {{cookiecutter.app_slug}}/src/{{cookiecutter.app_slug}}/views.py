{% if cookiecutter.create_copyright_notice == "y" %}
  {%- include "resources/copyright/header.txt" %}
{% endif -%}

from django.views.generic import TemplateView

{% if cookiecutter.create_project == "y" %}
class IndexView(TemplateView):
    template_name = "{{ cookiecutter.app_slug }}/index.html"
{%- endif %}
