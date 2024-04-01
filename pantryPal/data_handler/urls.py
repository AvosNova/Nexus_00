from django.urls import path
from .views import get_recipes , process_search_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', get_recipes, name='get_recipes'),
     path('search/', process_search_view, name='process_search'),
]
