from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Sample(models.Model):
    """
    A very basic sample model.
    """
    title = models.CharField(
        _("title"),
        blank=False,
        max_length=255,
        default="",
    )
    """
    Required unique title string.
    """

    slug = models.SlugField(
        _("slug"),
        max_length=255,
    )
    """
    Required unique slug string.
    """

    class Meta:
        ordering = ["title"]
        verbose_name = _("Sample")
        verbose_name_plural = _("Samples")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Return absolute URL to detail view.

        Returns:
            string: An URL.
        """
        return reverse("{{ cookiecutter.application_module }}:sample-detail", kwargs={
            "slug": self.slug,
        })
