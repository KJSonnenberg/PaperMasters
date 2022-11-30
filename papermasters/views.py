from django.shortcuts import render
#from papermasters.models import ModelClassName

def home(request):
    return render(request, 'papermasters/home.html') 