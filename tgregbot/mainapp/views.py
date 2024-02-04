from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse("Hello, world!")


def message(request):
    cur_message = "Привет!"
    return render(request, "mainapp/index.html", {"message": cur_message})

