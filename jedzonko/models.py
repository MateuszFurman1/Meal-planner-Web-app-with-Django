from django.db import models
from autoslug import AutoSlugField

class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True)  #
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    preparation_time = models.PositiveIntegerField()
    votes = models.PositiveIntegerField(blank=True, null=True)
    preparation_description = models.TextField()

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    recipes = models.ManyToManyField(Recipe, through='RecipePlan')

    def __str__(self):
        return self.name


class DayName(models.Model):
    name = models.CharField(max_length=64, unique=True)
    order = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=64)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    # order = models.PositiveIntegerField(unique=True)
    day = models.ForeignKey(DayName, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'plan')

    def __str__(self):
        return f'{self.recipe} {self.plan}' #{self.order}'


class Page(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from='title')

    def slugify_function(self, content):
        return content.replace('_', '-').lower()
