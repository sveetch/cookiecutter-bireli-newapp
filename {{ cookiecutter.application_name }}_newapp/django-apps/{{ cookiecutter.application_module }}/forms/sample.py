from django import forms

from ..models import Sample


class SampleAdminForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = "__all__"
