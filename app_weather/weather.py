from django.conf import settings

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from translate import Translator


def get_result_weather(locate):
    # locate_eu = get_translate_into_eu(locate)
    weather = get_weather(locate)

    return weather


def get_weather(locate):
    try:
        owm = OWM(settings.OPENWEATHER_API_KEY)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(locate)
        w = observation.weather

        status_ru = get_translate_into_ru(w.detailed_status)
        status_ru_eu = status_ru + ' / ' + w.detailed_status
        dict_weather = {'status': status_ru_eu, 'temperature': w.temperature('celsius'),
                        'wind': w.wind(), 'humidity': w.humidity, }

        return dict_weather

    except Exception:
        return False
#
#
# def get_translate_into_eu(word: str) -> str:
#     translator = Translator(from_lang='ru', to_lang="en")
#     translation = translator.translate(word)
#
#     return translation
#
#
# def get_translate_into_ru(word: str) -> str:
#     translator = Translator(from_lang='en', to_lang="ru")
#     translation = translator.translate(word)
#
#     return translation

