import factory.fuzzy

from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'User_{n}')
    password = factory.fuzzy.FuzzyText(length=12)




