from django.shortcuts import render, redirect
from django.conf import settings

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from translate import Translator

from .forms import LocateForm
from .weather import get_result_weather


def index(request):
    data_dict = {'locate': "Moscow", 'weather': get_result_weather('Moscow'), 'error': '', }

    form = LocateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data_dict['locate'] = form.cleaned_data.get("locate")
            data_dict['weather'] = get_result_weather(data_dict['locate'])
            if data_dict['weather'] == False:
                data_dict['error'] = "Некорректно введен город!"
                data_dict['locate'] = ""
            else:
                data_dict['error'] = ""

    data = {
        "weather": data_dict['weather'],
        'locate': data_dict['locate'].title(),
        'form': form,
        "error": data_dict['error'],
    }

    return render(request, 'app_weather/index.html', data)

