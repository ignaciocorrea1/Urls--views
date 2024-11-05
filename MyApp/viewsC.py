from django.shortcuts import render

def indexC(request):
    context = {}
    return render(request, "pages/c.html", context)