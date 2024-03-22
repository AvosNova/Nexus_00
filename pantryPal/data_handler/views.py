from django.shortcuts import render
from django.http import HttpResponse

import pymongo
from .config import API_key
import requests

uri = "mongodb+srv://pantrypal.slbncjm.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=pantryPal"

def index(request):
    return render(request, 'data_handler/index.html')

def get_recipes(request):
    url = "https://api.spoonacular.com/recipes/random"
    params = {
        'apiKey' : API_key,
        'number' : 3
    }

    response = requests.get(url, params=params)
    data = response.json()

    recipes = data.get('recipes', [])

    client = pymongo.MongoClient

    template_data = {'recipes': recipes}
    return render(request, 'data_handler/recipes.html', template_data)