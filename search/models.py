from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime
# Create your models here.


class Search(models.Model):
    # add fields that should be represented in the database and in the search feature
    job = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    radius = models.CharField(max_length=200)
    remote = models.CharField(max_length=200)
    hybrid = models.CharField(max_length=200)
    inperson = models.CharField(max_length=200)
    min_salary = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    job_time = models.CharField(max_length=200)
    max_ed = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)

