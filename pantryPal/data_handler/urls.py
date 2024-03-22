from django.urls import path
from .views import get_recipes
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', get_recipes, name='get_recipes'),
]
