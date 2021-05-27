from django.urls import path

from django101.cities.views import list_cities

urlpatterns = [
    path('cities/', list_cities),
]