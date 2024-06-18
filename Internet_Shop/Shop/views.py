from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hi! This is a internet shop.")
