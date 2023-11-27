from django.shortcuts import render
import pdb
from search.models import Search

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, "search/index.html")


def search(request):
    return render(request, "search/search.html")

def return_to_search(request):
    """search2 = Search.objects.get(id=Search.objects.count())
    # https://stackoverflow.com/questions/68106874/easiest-way-to-display-django-model-data-in-html
    context = {

        'search2': search2,

    }"""

    return render(request, "search/return_to_search.html", context)


def submit(request):
    job_title = request.POST.get('jobtitle', "None")  # make sure pick the right job title of chef
    salary = request.POST.get('salary', "None")  # check if equal to 16.75
    industry = request.POST.get('industry', "None")  # check if pick Food Service
    city = request.POST.get('city', "None")  # check if entered Charlottesville
    state = request.POST.get('state', "None")  # check if pick VA
    radius = request.POST.get('radius', "None")  # check if pick 10 miles
    remote = request.POST.get('remote', "None")  # check if pick remote
    hybrid = request.POST.get('hybrid', "None")  # check if pick hybrid
    inperson = request.POST.get('inperson', "None")  # check if pick inperson
    time = request.POST.get('time', 'Part-Time')  # value is 'time'
    maxed = request.POST.get('maxed', "None")  # check if pick hs
    fieldofstudy = request.POST.get('fieldofstudy', "None")  # check if pick culinary arts
    # create a new search object-- Search(job=job_title, city=city, state=state,radius=radius, remote = remote, hybrid=hybrid, inperson=inperson, min_salary=salary, industry = industry, job_time = time, max_ed = maxed, field_of_study =fieldofstudy)
    #  Search.objects.all()
    #  Search.objects.filter(id=1)
    #  Search.objects.count()
    search1 = Search(job=str(job_title).capitalize(), city=str(city).capitalize(), state=str(state).upper(), radius=radius, remote=remote, hybrid=hybrid,
                     inperson=inperson, min_salary=salary, industry=industry, job_time=time, max_ed=maxed,
                     field_of_study=fieldofstudy)

    search1.save()  # save the class

    # Search.all()
    """if str(time) == "Full-Time":
        pdb.set_trace()

        print('hi')
    elif str(time) == "Part-Time":
        pdb.set_trace()

        print('bye')"""
    if str(job_title).casefold().strip() in ["chef"] and str(salary).strip() == '16.75' and str(maxed).casefold() in [
        "hs"] and str(industry).casefold() in ["foodservice"] and str(city).casefold().strip() in [
        "charlottesville"] and str(state).casefold() in ["va"] and str(radius).casefold() in [
        "10"] and remote == "None" and hybrid == "None" and str(inperson).casefold() == "inperson" and str(
            fieldofstudy).casefold().strip() in ["culinary arts", "culinary  arts", "culinary   arts"] and str(
            time) == "Full-Time":

        return render(request, "search/results.html")
    else:

        search2 = Search.objects.get(id=Search.objects.count())
        # https://stackoverflow.com/questions/68106874/easiest-way-to-display-django-model-data-in-html
        context = {

            'search2': search2,
            "hello": "hi"

        }
        return render(request, "search/no_results.html", context)


def results(request):
    return render(request, "search/results.html")

def resultsnone(request):
    return render(request, "search/no_results.html")


def results2(request):
    return render(request, "search/results_bysalary.html")


def not_yet_implemented(request):
    return render(request, "search/not_yet_implemented.html")
