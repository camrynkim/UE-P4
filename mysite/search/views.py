from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, "search/index.html")


def search(request):
    return render(request, "search/search.html")


def results(request):
    return render(request, "search/results.html")


def not_yet_implemented(request):
    return render(request, "search/not_yet_implemented.html")

