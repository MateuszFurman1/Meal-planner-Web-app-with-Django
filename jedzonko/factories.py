import factory
from .models import Recipe, Plan, DayName, RecipePlan, Page


class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe

    name = factory.Faker('name')
    ingredients = factory.Faker('text', max_nb_chars=30)
    description = factory.Faker('text', max_nb_chars=50)
    created = factory.Faker('date_time_this_month', tzinfo=None)
    updated = factory.Faker('date_time_this_month', tzinfo=None)
    preparation_time = factory.Faker('random_int', min=10, max=240)
    votes = factory.Faker('random_int', min=1, max=99)
    preparation_description = factory.Faker('text', max_nb_chars=50)


class PlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Plan

    name = factory.Faker('sentence', nb_words=10)
    description = factory.Faker('text', max_nb_chars=50)
    created = factory.Faker('date_time_this_month', tzinfo=None)


class DayNameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DayName

    name = factory.Faker('word')
    order = factory.Sequence(lambda n: n % 7 + 1)


class RecipePlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RecipePlan

    meal_name = factory.Faker('word')
    recipe = factory.SubFactory(RecipeFactory)
    plan = factory.SubFactory(PlanFactory)
    order = factory.Sequence(lambda n: n)
    day = factory.SubFactory(DayNameFactory)


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Page

    title = factory.Faker('sentence', nb_words=5)
    description = factory.Faker('text', max_nb_chars=50)
