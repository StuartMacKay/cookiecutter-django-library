{% if cookiecutter.create_copyright_notice == "y" %}
  {%- include "resources/copyright/header.txt" %}
{% endif -%}

from django.urls import path

{% if cookiecutter.create_project %}from .views import IndexView{% endif %}

urlpatterns = [{% if cookiecutter.create_project %}path("", IndexView.as_view(), name="app_index"){% endif %}]
