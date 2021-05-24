from django.shortcuts import render

from django101.cities.models import Person


def index(req):
    context = {
        "name": "Debora",
        "people": Person.objects.all()
    }
    return render(req, 'index.html', context)
