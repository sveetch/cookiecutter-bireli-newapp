from project_composer.marker import EnabledApplicationMarker


class {{ cookiecutter.application_class }}Settings(EnabledApplicationMarker):
    """
    {{ cookiecutter.application_class }} settings
    """
    {{ cookiecutter.application_class.upper() }}_SAMPLE_PAGINATION = 10

    @classmethod
    def post_setup(cls):
        super({{ cookiecutter.application_class }}Settings, cls).post_setup()

        cls.INSTALLED_APPS.extend([
            "{{ cookiecutter.application_module }}",
        ])
