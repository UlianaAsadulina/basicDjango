from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return HttpResponse("Home Page")

def index(response):
    return HttpResponse("Index Page")