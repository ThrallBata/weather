from django.shortcuts import render
from django.conf import settings

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


def index(request):
    name = 'Hirt'
    locate = 'Tomsk'
    weather = get_weather(locate)

    data = {
        'name': name,
        "weather": weather,
        'locate': locate,
    }

    return render(request, 'app_weather/index.html', data)


def get_weather(locate):
    owm = OWM(settings.OPENWEATHER_API_KEY)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(locate)
    w = observation.weather

    dict_weather = {'status': w.detailed_status, 'temperature': w.temperature('celsius'),
                    'wind': w.wind(), 'humidity': w.humidity}

    return dict_weather