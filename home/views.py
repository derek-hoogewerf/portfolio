# Create your views here.
import re
import os
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import redirect, render
from home.forms import LogMessageForm
from home.models import LogMessage
from web_project.settings import STATIC_ROOT

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

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

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "home/log_message.html", {"form": form})