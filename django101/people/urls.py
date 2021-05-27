from django.urls import path

from django101.people.views import list_people

urlpatterns = [
    path('people/', list_people),
]