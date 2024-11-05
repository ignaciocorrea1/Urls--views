from django.shortcuts import render

# Create your views here.
def indexD(request):
    context = {}
    return render(request, "pages/d.html", context)