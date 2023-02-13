from django.urls import path

from .views import SampleIndexView, SampleDetailView


app_name = "{{ cookiecutter.application_module }}"


urlpatterns = [
    path("samples/", SampleIndexView.as_view(), name="sample-index"),
    path(
        "samples/<slug:slug>/",
        SampleDetailView.as_view(),
        name="sample-detail"
    ),
]
