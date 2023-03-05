from django.shortcuts import render


def index(request):
    name = 'Hirt'

    data = {
        'name': name,
    }

    return render(request, 'app_weather/index.html', data)

