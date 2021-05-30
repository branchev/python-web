from django.shortcuts import render, redirect

from django101.cities.models import Person


def index(req):
    context = {
        "name": "Debora",
        "people": Person.objects.all()
    }
    return render(req, 'index.html', context)


def list_cities(req):
    context = {
        "cities": [
            "Sofia",
            "Plovdiv",
            "Varna",
            "Burgas"
        ]
    }
    return render(req, 'cities.html', context)


def create_person(req):
    Person(
        name="Gitka",
        age=20,
        home_town="Bosilegrad"
    ).save()

    return redirect('/')
