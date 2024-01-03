from datetime import datetime
from django.shortcuts import render, redirect
from . models import About


# Create your views here.

def homeindex(request):
    return render(request, "secdemport/index.html")

def about(request):
    return render(request, "admin/about.html")

def insert(request):
    name = request.POST.get('name')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    yearsExperience = request.POST.get('yearsExperience')
    happyCustomers = request.POST.get('happyCustomers')
    projectsFinished = request.POST.get('projectsFinished')
    digitalAwards = request.POST.get('digitalAwards')
    description = request.POST.get('description')
    dateTime = datetime.now()
    formatted_datetime = dateTime.strftime("%d %b %Y - %I:%M %p")


    aboutObj = About()

    aboutObj.name = name
    aboutObj.dob = dob
    aboutObj.phone = phone
    aboutObj.email = email
    aboutObj.yearsExperience = yearsExperience
    aboutObj.happyCustomers = happyCustomers
    aboutObj.projectsFinished = projectsFinished
    aboutObj.digitalAwards = digitalAwards
    aboutObj.description = description
    aboutObj.dateTime = formatted_datetime

    aboutObj.save()

    return redirect('about')
