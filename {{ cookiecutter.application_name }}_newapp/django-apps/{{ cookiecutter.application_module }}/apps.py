from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class {{ cookiecutter.application_class }}Config(AppConfig):
    name = "{{ cookiecutter.application_module }}"
    verbose_name = _("{{ cookiecutter.application_title.replace('"', "'") }}")
    default_auto_field = "django.db.models.AutoField"
