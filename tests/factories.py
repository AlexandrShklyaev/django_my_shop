import factory

from ads.models import Ad, Category
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    slug = factory.Faker("color")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "test2"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    author = factory.SubFactory(UserFactory)
    price = 100
    category = factory.SubFactory(CategoryFactory)
