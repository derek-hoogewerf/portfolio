from django.shortcuts import render

# Create your views here.
import re
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")
Run the app#

def hello_there(request, name):
    return render(
        request,
        'home/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )