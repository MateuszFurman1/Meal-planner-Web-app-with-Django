from django.urls import reverse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from random import choice
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from jedzonko.models import *
from django.core.paginator import Paginator
from .form import PlanForm, RecipeForm, RecipePlanForm, RecipeVotesForm, RegistrationForm, LoginForm, UserUpdateForm


class IndexView(View):
    '''
    Home page
    Show 3 last recipes added to system.
    In navbar user can move to about, contact and panel section.
    return index templates
    '''
    def get(self, request):
        recipes = list(Recipe.objects.all())
        page = Page.objects.get(pk=1)
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
            'page': page,

        }
        return render(request, "index.html", ctx)


class RecipeListView(LoginRequiredMixin, View):
    '''
    Show all recipes
    User can add recipe, recipe to plan.
    User can also delete, edit and go to detail
    Require login user
    return app-recipe templates
    '''
    login_url = "/login/"

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
    '''
    Display panel where user can add recipe, recipe do plan and plan
    return dashboard templates
    '''
    def get(self, request):
        plans = Plan.objects.count()
        recipes = Recipe.objects.count()
        days = DayName.objects.all().order_by("order")
        plan = Plan.objects.all().order_by("-id").first()
        recipe_plans_pon = RecipePlan.objects.filter(plan=plan).filter(day=days[0])
        recipe_plans_wt = RecipePlan.objects.filter(plan=plan).filter(day=days[1])
        recipe_plans_sr = RecipePlan.objects.filter(plan=plan).filter(day=days[2])
        recipe_plans_czw = RecipePlan.objects.filter(plan=plan).filter(day=days[3])
        recipe_plans_pia = RecipePlan.objects.filter(plan=plan).filter(day=days[4])
        recipe_plans_sob = RecipePlan.objects.filter(plan=plan).filter(day=days[5])
        recipe_plans_nl = RecipePlan.objects.filter(plan=plan).filter(day=days[6])

        ctx = {
            "plans": plans,
            "recipes": recipes,
            'recipe_plans_pon': recipe_plans_pon,
            'recipe_plans_wt': recipe_plans_wt,
            'recipe_plans_sr': recipe_plans_sr,
            'recipe_plans_czw': recipe_plans_czw,
            'recipe_plans_pia': recipe_plans_pia,
            'recipe_plans_sob': recipe_plans_sob,
            'recipe_plans_nl': recipe_plans_nl,
            'plan': plan,
        }
        return render(request, "dashboard.html", ctx)


class PlanListView(LoginRequiredMixin, View):
    '''
    Show all plans
    User can add plan and recipe to plan.
    User can also delete, edit and go to detail
    Require login user
    return app-schedules templates
    '''
    login_url = "/login/"

    def get(self, request):
        plans_list = Plan.objects.all().order_by('name')
        p = Paginator(plans_list, 2)
        page = request.GET.get('page')
        plans = p.get_page(page)
        ctx = {
            "plans": plans,
        }
        return render(request, "app-schedules.html", ctx)


class AddRecipeView(LoginRequiredMixin, View):
    '''
    Show all plans
    User can add plan and recipe to plan.
    User can also delete, edit and go to detail
    Require login user
    return app-schedules templates
    '''
    login_url = "/login/"

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


class RecipeUpdateView(LoginRequiredMixin, View):
    login_url = "/login/"

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
        message = "Wypełnij poprawnie pola"
        if form.is_valid():
            r = form.save()
            return redirect('recipe-detail', r.id)
        ctx = {
            'form': form,
            'message': message
        }
        return render(request, 'recipe_update_form.html', ctx)


class RecipeDeleteView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        recipe.delete()
        return redirect(reverse('recipee-list'))


class AddPlanView(LoginRequiredMixin, View):
    login_url = "/login/"

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


class AddRecipeToPlanView(LoginRequiredMixin, View):
    login_url = "/login/"

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


class RecipeDetailView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(pk=recipe_id)
        recipe_ingredians = recipe.ingredients.splitlines()
        ctx = {
            "recipe": recipe,
            "recipe_ingredians": recipe_ingredians,
        }
        return render(request, 'app-recipe-details.html', ctx)

    def post(self, request, recipe_id):
        form = RecipeVotesForm(request.POST)
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        if 'like' in request.POST:
            if form.is_valid():
                recipe.votes +=1
                recipe.save()
        else:
            if form.is_valid():
                recipe.votes -=1
                recipe.save()
        return redirect('recipe-detail', recipe.id)


class PlanDetails(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, plan_id):
        plan = Plan.objects.get(pk=plan_id)
        days = DayName.objects.all().order_by("order")
        recipe_plans_pon = RecipePlan.objects.filter(plan=plan).filter(day=days[0])
        recipe_plans_wt = RecipePlan.objects.filter(plan=plan).filter(day=days[1])
        recipe_plans_sr = RecipePlan.objects.filter(plan=plan).filter(day=days[2])
        recipe_plans_czw = RecipePlan.objects.filter(plan=plan).filter(day=days[3])
        recipe_plans_pia = RecipePlan.objects.filter(plan=plan).filter(day=days[4])
        recipe_plans_sob = RecipePlan.objects.filter(plan=plan).filter(day=days[5])
        recipe_plans_nl = RecipePlan.objects.filter(plan=plan).filter(day=days[6])
        days = DayName.objects.all().order_by("order")
        ctx = {
            'plan': plan,
            'recipe_plans_pon': recipe_plans_pon,
            'recipe_plans_wt': recipe_plans_wt,
            'recipe_plans_sr': recipe_plans_sr,
            'recipe_plans_czw': recipe_plans_czw,
            'recipe_plans_pia': recipe_plans_pia,
            'recipe_plans_sob': recipe_plans_sob,
            'recipe_plans_nl': recipe_plans_nl,
            'days': days,
        }
        return render(request, 'app-details-schedules.html', ctx)


class PlanUpdateView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, plan_id):
        plan = get_object_or_404(Plan, id=plan_id)
        form = PlanForm(instance=plan)
        ctx = {
            'form': form
        }
        return render(request, 'plan_update_form.html', ctx)

    def post(self, request, plan_id):
        plan = get_object_or_404(Plan, id=plan_id)
        form = PlanForm(request.POST, instance=plan)
        message = "Wypełnij poprawnie pola"
        if form.is_valid():
            r = form.save()
            return redirect('plan-details', r.id)
        ctx = {
            'form': form,
            'message': message
        }
        return render(request, 'plan_update_form.html', ctx)


class PlanDeleteView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, plan_id):
        plan = get_object_or_404(Plan, id=plan_id)
        plan.delete()
        return redirect(reverse('plan-list'))


class RecipePlanEditView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, recipe_plan_id):
        recipe_plan = RecipePlan.objects.get(pk=recipe_plan_id)
        plan = recipe_plan.plan
        form = RecipePlanForm(instance=recipe_plan)
        ctx = {
            'recipe_plan': recipe_plan,
            'plan': plan,
            'form': form,
        }
        return render(request, 'recipe_plan-details.html', ctx)

    def post(self, request, recipe_plan_id):
        recipe_plan = RecipePlan.objects.get(pk=recipe_plan_id)
        form = RecipePlanForm(request.POST, instance=recipe_plan)
        message = "Wypełnij poprawnie pola"
        if form.is_valid():
            r = form.save()
            return redirect('plan-details', r.id)
        ctx = {
            'form': form,
            'message': message
        }
        return render(request, 'recipe_plan-details.html', ctx)


class RecipePlanDeleteView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, recipe_plan_id):
        recipe_plan = get_object_or_404(RecipePlan, id=recipe_plan_id)
        recipe_plan.delete()
        return redirect('plan-details', recipe_plan.plan_id)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        page = 'login'
        ctx = {
            "form": form,
            'page': page
        }
        return render(request, 'form.html', ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        ctx = {
            "form": form,
        }
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            ctx = {
                "form": form
            }
        return render(request, 'form.html', ctx)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        page = 'registration'
        ctx = {
            "form": form,
            'page': page
        }
        return render(request, "registration_form.html", ctx)

    def post(self, request):
        form = RegistrationForm(request.POST)
        ctx = {
            "form": form,
        }
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')

        return render(request, 'registration_form.html', ctx)


class ProfileView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        user = request.user
        form = UserUpdateForm(instance=user)
        ctx = {
            'form': form,
        }
        return render(request, "profile.html", ctx)

    def post(self, request):
        user = request.user
        form = UserUpdateForm(request.POST, instance=user)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'profile.html', ctx)