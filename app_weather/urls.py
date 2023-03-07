from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    #path('/weather', weather_locate, name='weather')
]
