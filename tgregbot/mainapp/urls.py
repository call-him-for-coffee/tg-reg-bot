from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("login/<int:chat_id>/", views.login, name="login")
]
