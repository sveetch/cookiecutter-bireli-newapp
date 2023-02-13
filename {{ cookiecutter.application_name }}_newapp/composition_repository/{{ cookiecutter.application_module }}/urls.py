from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

from project_composer.marker import EnabledApplicationMarker


class {{ cookiecutter.application_class }}Urls(EnabledApplicationMarker):
    """
    {{ cookiecutter.application_class }} urls
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        if self.settings.ENABLE_I18N_URLS:
            return urlpatterns + i18n_patterns(
                path("{{ cookiecutter.application_name }}/", include("{{ cookiecutter.application_module }}.urls")),
            )
        else:
            return urlpatterns + [
                path("{{ cookiecutter.application_name }}/", include("{{ cookiecutter.application_module }}.urls")),
            ]
