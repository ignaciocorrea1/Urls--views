from django.urls import path
from MyApp import viewsI

urlpatterns = [
    path("", viewsI.index, name="index"),
]