from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


def weather_view(request, city):
    if city in weather_data:
        return JsonResponse(weather_data[city])
    else:
        raise Http404("City not found")