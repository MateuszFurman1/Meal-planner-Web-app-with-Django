"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jedzonko.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='homepage'),
    path('recipe/list/', RecipeListView.as_view(), name='recipee-list'),
    path('main/', DashboardView.as_view(), name='dashboard'),
    path('plan/list/', PlanListView.as_view(), name='plan-list'),
    path('recipe/add/', AddRecipeView.as_view(), name='recipe-add'),
    path('plan/add/', AddPlanView.as_view(), name='plan-add'),
    path('plan/add-recipe/', AddRecipeToPlanView.as_view(), name='plan-add-recipe'),
    path('recipe/<int:recipe_id>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('plan/<int:plan_id>', PlanDetails.as_view(), name='plan-details'),
    path('recipe/edit/<int:recipe_id>', RecipeUpdateView.as_view(), name='recipe-edit'),
    path('recipe/delete/<int:recipe_id>', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('plan/edit/<int:plan_id>', PlanUpdateView.as_view(), name='plan-edit'),
    path('plan/delete/<int:plan_id>', PlanDeleteView.as_view(), name='plan-delete'),
    path('recipe_plan/edit/<int:recipe_plan_id>', RecipePlanEditView.as_view(), name='recipe_plan-edit'),
    path('recipe_plan/delete/<int:recipe_plan_id>', RecipePlanDeleteView.as_view(), name='recipe_plan-delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reistration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
