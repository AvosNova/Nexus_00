from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt #need this otherwise Django gives csrf error
def process_search(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        #Placeholder response
        return HttpResponse(f"You entered: {input_text}")
    else:
        # Display the form
        return render(request, 'data_handler/search.html')