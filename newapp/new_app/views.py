from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def home(response):
    return HttpResponse("Home Page")

def index(response, id):
    current_list = ToDoList.objects.get(id=id)
    items = current_list.item_set.get(id=1)
    return HttpResponse("<h1> %s </h1><p>%s</p> " %(current_list.name, str(items.text)) )