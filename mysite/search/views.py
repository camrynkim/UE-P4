from django.shortcuts import render
import pdb

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, "search/index.html")


def search(request):
    return render(request, "search/search.html")


def submit(request):
    job_title = request.POST["jobtitle"]  # make sure pick the right job title of chef
    salary = request.POST["salary"]  # check if equal to 16.75
    industry = request.POST["industry"]  # check if pick Food Service
    city = request.POST["city"]  # check if entered Charlottesville
    state = request.POST["state"]  # check if pick VA
    radius = request.POST["radius"]  # check if pick 10 miles
    remote = request.POST.get('remote', False)  # check if pick remote
    hybrid = request.POST.get('hybrid', False)  # check if pick hybrid
    inperson = request.POST.get('inperson', False)  # check if pick inperson
    time = request.POST.get('time', 'Part-Time')  # value is 'time'
    maxed = request.POST["maxed"]  # check if pick hs
    fieldofstudy = request.POST["fieldofstudy"]  # check if pick culinary arts
    """if str(time) == "Full-Time":
        pdb.set_trace()

        print('hi')
    elif str(time) == "Part-Time":
        pdb.set_trace()

        print('bye')"""
    if str(job_title).casefold() in ["chef"] and str(salary) == '16.75' and str(maxed).casefold() in ["hs"] and str(industry).casefold() in ["foodservice"] and str(city).casefold() in ["charlottesville"] and str(state).casefold() in ["va"] and str(radius).casefold() in ["10"] and remote == False and hybrid == False and str(inperson).casefold() == "inperson" and str(fieldofstudy).casefold() == "culinary arts" and str(time) == "Full-Time":

        return render(request, "search/results.html")
    else:
        return render(request, "search/error.html")


def results(request):
    return render(request, "search/results.html")


def not_yet_implemented(request):
    return render(request, "search/not_yet_implemented.html")
