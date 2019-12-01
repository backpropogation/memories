import factory.fuzzy

from apps.memories.models import Memory
from apps.users.factory import UserFactory


class MemoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Memory

    title = factory.Sequence(lambda n: f'Memory_{n}')
    description = factory.Faker('text')
    longitude = factory.fuzzy.FuzzyFloat(low=0.0, high=100.00)
    latitude = factory.fuzzy.FuzzyFloat(low=0.0, high=100.00)
    owner = factory.SubFactory(UserFactory)
