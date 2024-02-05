from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import MyUser


def start(request):
    return render(request, "mainapp/index.html")


def login(request, chat_id):
    try:
        user = MyUser.objects.get(chat_id = chat_id)
    except MyUser.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, "mainapp/logged.html", {"username": user})
