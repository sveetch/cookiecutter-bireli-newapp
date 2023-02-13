import factory

from ..models import Sample


class SampleFactory(factory.django.DjangoModelFactory):
    """
    Factory to create an instance of a Sample.
    """
    title = factory.Sequence(lambda n: "Sample {0}".format(n))
    slug = factory.Sequence(lambda n: "sample-{0}".format(n))

    class Meta:
        model = Sample
