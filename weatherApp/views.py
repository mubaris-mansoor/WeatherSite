from django.shortcuts import render

# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=cf04bb1c1cbb56802202f29873defeb9'

    city = 'Manama'

    city_weather = requests.get(url.format(city)).json() #we are requesting the API data and converting the JSON to Python data types
    print(city_weather) #checking the output
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'wind' : city_weather['wind']['speed'],
        'icon' : city_weather['weather'][0]['icon']
    }
    return render(request, 'index.html', {'weather' : weather}) #returns the index.html template

    