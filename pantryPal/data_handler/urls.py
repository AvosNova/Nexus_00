from django.urls import path
from .views import get_recipes

urlpatterns = [
    path('recipes/', get_recipes, name='get_recipes'),
]
