from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def list_people(req):
    return HttpResponse('People list', list_people)
