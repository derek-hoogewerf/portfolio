from django.shortcuts import render

# Create your views here.
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
import os
from web_project.settings import STATIC_ROOT

def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

def hello_there(request, name):
    return render(
        request,
        'home/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )