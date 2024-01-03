from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length = 500)
    dob = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    yearsExperience = models.CharField(max_length = 500)
    happyCustomers = models.CharField(max_length = 500)
    projectsFinished = models.CharField(max_length = 500)
    digitalAwards = models.CharField(max_length = 500)
    description = models.CharField(max_length = 500)
    dateTime = models.CharField(max_length = 500)
