from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(response, "register/register.html", {"form": form})
