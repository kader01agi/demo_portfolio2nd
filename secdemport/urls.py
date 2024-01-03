from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeindex, name= "homeindex"),
    path('about/', views.about, name= "about"),
    path('insert/', views.insert, name= "insert")
]