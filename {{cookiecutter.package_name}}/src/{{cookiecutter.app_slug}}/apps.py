{% if cookiecutter.create_copyright_notice == "y" %}
  {%- include "resources/copyright/header.txt" %}
{% endif -%}
from django.apps import AppConfig


def setup_app_settings():
    from django.conf import settings

    from . import settings as defaults

    for name in dir(defaults):
        if name.isupper() and not hasattr(settings, name):
            setattr(settings, name, getattr(defaults, name))


class {{ cookiecutter.app_config }}(AppConfig):
    name = "{{ cookiecutter.app_slug }}"
    verbose_name = "{{ cookiecutter.app_name }}"

    def ready(self):
        setup_app_settings()
