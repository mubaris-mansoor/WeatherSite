from django.shortcuts import render

# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=cf04bb1c1cbb56802202f29873defeb9'

    cityHome = 'Manama'

    cityHome_weather = requests.get(url.format(cityHome)).json() #we are requesting the API data and converting the JSON to Python data types
    print(cityHome_weather)
    weatherHome = {
        'city' : cityHome,
        'temperature' : cityHome_weather['main']['temp'],
        'description' : cityHome_weather['weather'][0]['description'],
        'wind' : cityHome_weather['wind']['speed'],
        'icon' : cityHome_weather['weather'][0]['icon'],
        'country' : cityHome_weather['sys']['country']
    }

    cityAway = 'Pune'

    cityAway_weather = requests.get(url.format(cityAway)).json() #we are requesting the API data and converting the JSON to Python data types
    print(cityAway_weather)
    weatherAway = {
        'city' : cityAway,
        'temperature' : cityAway_weather['main']['temp'],
        'description' : cityAway_weather['weather'][0]['description'],
        'wind' : cityAway_weather['wind']['speed'],
        'icon' : cityAway_weather['weather'][0]['icon'],
        'country' : cityAway_weather['sys']['country']
    }
    return render(request, 'index.html', {'weatherHome' : weatherHome, 'weatherAway' : weatherAway}) #returns the index.html template

# def index1(request1):
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=cf04bb1c1cbb56802202f29873defeb9'


#     return render(request1, 'index.html', {'weatherAway' : weatherAway}) #returns the index.html template




    