from django.urls import path
from MyApp import viewsD

urlpatterns = [
    path("indexD", viewsD.indexD, name="indexD"),
]