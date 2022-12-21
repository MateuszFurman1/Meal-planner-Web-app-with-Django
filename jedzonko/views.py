from django.urls import reverse
from datetime import datetime
from random import choice
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from jedzonko.models import *
from django.core.paginator import Paginator
from .form import PlanForm, RecipeForm, RecipePlanForm


class IndexView(View):

    def get(self, request):
        recipes = list(Recipe.objects.all())
        recipe0 = ''
        recipe1 = ''
        recipe2 = ''
        if recipes:
            recipe0 = choice(recipes)
            recipes.remove(recipe0)
            recipe1 = choice(recipes)
            recipes.remove(recipe1)
            recipe2 = choice(recipes)
        ctx = {
            "actual_date": datetime.now(),
            "recipe0": recipe0,
            "recipe1": recipe1,
            "recipe2": recipe2,

        }
        return render(request, "index.html", ctx)


class RecipeListView(View):

    def get(self, request):
        recipes_list = Recipe.objects.all().order_by('-votes', '-created')
        p = Paginator(recipes_list, 50)
        page = request.GET.get('page')
        recipes = p.get_page(page)

        ctx = {
            "recipes": recipes,
        }
        return render(request, "app-recipes.html", ctx)


class DashboardView(View):

    def get(self, request):
        plans = Plan.objects.count()
        recipes = Recipe.objects.count()
        ctx = {
            "plans": plans,
            "recipes": recipes,
        }
        return render(request, "dashboard.html", ctx)


class PlanListView(View):

    def get(self, request):
        plans_list = Plan.objects.all().order_by('name')
        p = Paginator(plans_list, 2)
        page = request.GET.get('page')
        plans = p.get_page(page)
        ctx = {
            "plans": plans,
        }
        return render(request, "app-schedules.html", ctx)


class AddRecipeView(View):

    def get(self, request):
        form = RecipeForm()
        ctx = {
            'form': form
        }
        return render(request, 'app-add-recipe.html', ctx)

    def post(self, request):
        form = RecipeForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('recipee-list')
        return render(request, 'app-add-recipe.html', ctx)


class RecipeUpdateView(View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = RecipeForm(instance=recipe)

        ctx = {
            'form': form
        }
        return render(request, 'recipe_update_form.html', ctx)

    def post(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            r = form.save()
            return redirect('recipe-detail', r.id)
        ctx = {
            'form': form
        }
        return render(request, 'recipe_update_form.html', ctx)


class RecipeDeleteView(View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        recipe.delete()
        return redirect(reverse('recipee-list'))


class AddPlanView(View):

    def get(self, request):
        form = PlanForm()

        ctx = {
            'form': form
        }
        return render(request, 'app-add-schedules.html', ctx)

    def post(self, request):

        form = PlanForm(request.POST or None)
        if form.is_valid():
            p = form.save()
            return redirect('plan-details', p.id)
        else:
            form = PlanForm(request.POST or None)
            ctx = {
                'form': form
            }
            return render(request, 'app-add-schedules.html', ctx)


class AddRecipeToPlanView(View):
    def get(self, request):
        form = RecipePlanForm()
        ctx = {
            'form': form,
        }
        return render(request, 'app-schedules-meal-recipe.html', ctx)

    def post(self, request):
        form = RecipePlanForm(request.POST)
        if form.is_valid():
            p = form.save()
            print(p.plan)
            return redirect('plan-details', p.plan.id)
        ctx = {
            'form': form
        }
        return render(request, 'app-schedules-meal-recipe.html', ctx)

class RecipeDetailView(View):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(pk=recipe_id)
        recipe_ingredians = recipe.ingredients.splitlines()

        ctx = {
            "recipe": recipe,
            "recipe_ingredians": recipe_ingredians,
        }
        return render(request, 'app-recipe-details.html', ctx)


class PlanDetails(View):

    def get(self, request, plan_id):
        plan = Plan.objects.get(pk=plan_id)
        ctx = {
            'plan': plan,
        }
        return render(request, 'app-details-schedules.html', ctx)
