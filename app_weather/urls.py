from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('', start_page, name='start'),
    # path('weather', index, name='index')
]
