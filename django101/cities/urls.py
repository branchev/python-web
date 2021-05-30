from django.urls import path

from django101.cities.views import list_cities, create_person

urlpatterns = [
    path('', list_cities),
    path('create/', create_person),
]
