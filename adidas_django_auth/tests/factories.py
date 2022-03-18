from random import randint, uniform

import factory
from factory import LazyAttribute, LazyFunction, SubFactory, fuzzy
from factory.django import DjangoModelFactory
from faker import Factory

from adidas_django_auth.models import User

faker = Factory.create()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    role = fuzzy.FuzzyChoice(User.ROLE_CHOICES, getter=lambda c: c[0])
    dob = LazyFunction(faker.date)
    nationality = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    gender = fuzzy.FuzzyChoice(User.GENDER_CHOICES, getter=lambda c: c[0])
