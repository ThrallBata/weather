from django.shortcuts import render, redirect
from django.conf import settings

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from translate import Translator

from .forms import LocateForm


def index(request):
    form = LocateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            global locate
            locate = form.cleaned_data.get("locate")
            global weather
            weather = get_result_weather(locate)
            if weather == False:
                global error
                error = "Некорректно введен город!"
                locate = ""
            else:
                error = ""

    data = {
        "weather": weather,
        'locate': locate,
        'form': form,
        "error": error,
    }

    return render(request, 'app_weather/index.html', data)


# def weather_locate(request):
#     if request.method == 'POST':
#         print('govno')
#         if form.is_valid():
#             print('Sperma')
#             global locate
#             locate = form.cleaned_data.get("locate")
#             global weather
#             weather = get_result_weather(locate)
#
#
#     data = {
#         "weather": weather,
#         'locate': locate,
#         'form': form,
#     }
#
#     return render(request, 'app_weather/base1.html', data)


def get_result_weather(locate):
    locate_eu = get_translate_eu(locate)
    weather = get_weather(locate_eu)

    return weather


def get_weather(locate):
    try:
        owm = OWM(settings.OPENWEATHER_API_KEY)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(locate)
        w = observation.weather

        status_ru = get_translate_ru(w.detailed_status)
        status_ru_eu = status_ru + '/' + w.detailed_status
        dict_weather = {'status': status_ru_eu, 'temperature': w.temperature('celsius'),
                    'wind': w.wind(), 'humidity': w.humidity}

        print(dict_weather)
        return dict_weather

    except Exception:
        return False


def get_translate_eu(word: str) -> str:
    translator = Translator(from_lang='ru', to_lang="en")
    translation = translator.translate(word)

    return translation


def get_translate_ru(word: str) -> str:
    translator = Translator(from_lang='en', to_lang="ru")
    translation = translator.translate(word)

    return translation


locate = "Moscow"
weather = get_weather(locate)
error = ''



