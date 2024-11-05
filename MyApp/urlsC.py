from django.urls import path
from MyApp import viewsC

urlpatterns = [
    path("indexC", viewsC.indexC, name="indexC"),
]