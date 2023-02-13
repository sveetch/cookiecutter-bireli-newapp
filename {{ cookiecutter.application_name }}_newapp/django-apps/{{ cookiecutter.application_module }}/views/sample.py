from django.conf import settings
from django.views.generic import DetailView, ListView

from ..models import Sample


class SampleIndexView(ListView):
    """
    List of sample objects.
    """
    context_object_name = "sample_list"
    model = Sample
    paginate_by = settings.{{ cookiecutter.application_class.upper() }}_SAMPLE_PAGINATION
    template_name = "{{ cookiecutter.application_module }}/sample/index.html"
    ordering = model._meta.ordering

    def get_queryset(self):
        return self.model.objects.all()


class SampleDetailView(DetailView):
    """
    Sample detail view.
    """
    context_object_name = "sample_object"
    model = Sample
    slug_url_kwarg = "slug"
    template_name = "{{ cookiecutter.application_module }}/sample/detail.html"

    def get_queryset(self):
        return self.model.objects.all()
