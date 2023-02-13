from django.contrib import admin

from ..forms import SampleAdminForm
from ..models import Sample


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, {
                "fields": (
                    "title",
                    "slug",
                )
            }
        ),
    )
    form = SampleAdminForm
    list_display = (
        "title",
        "slug",
    )
    ordering = Sample._meta.ordering
    prepopulated_fields = {
        "slug": ("title",),
    }
    search_fields = [
        "title",
    ]
