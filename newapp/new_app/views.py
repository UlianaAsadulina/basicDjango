from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def home(response):
    return render(response, "new_app/home.html", {})

def index(response, id):
    current_list = ToDoList.objects.get(id=id)
    # items = current_list.item_set.get(id=1)
    return render(response, "new_app/list.html", {"current_list": current_list})