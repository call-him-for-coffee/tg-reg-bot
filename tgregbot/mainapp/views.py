from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import User


def index(request):
    return HttpResponse("Hello, world!")


def message(request):
    cur_message = "Привет!"
    return render(request, "mainapp/index.html", {"message": cur_message})


def start(request):
    cur_message = "Привет!"
    user = User(chat_id="1", phone_number="1")
    user.save()
    return render(request, "mainapp/index.html", {"message": user})
