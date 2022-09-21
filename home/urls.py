from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/<name>", views.hello_there, name="hello_there"),
]