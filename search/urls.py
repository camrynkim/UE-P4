"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notyetimplemented", views.not_yet_implemented, name="not_yet_implemented"),
    path("search", views.search, name="search"),
    path("search2", views.return_to_search, name="search2"),
    path("search/results", views.results, name="results"),
    path("search/submit", views.submit, name="submit"),
    path("search/results2", views.results2, name="results2"),
    path("search/resultsnone", views.resultsnone, name="resultsnone"),

]
