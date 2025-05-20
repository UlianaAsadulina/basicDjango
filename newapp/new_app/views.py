from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def home(response):
    return render(response, "new_app/home.html", {})

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # items = current_list.item_set.get(id=1)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text = txt, complete=False)
            else:
                print("invalid text for ToDo")

    return render(response, "new_app/list.html", {"ls": ls})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form=CreateNewList()
    return render(response, "new_app/create.html", {"form": form} )
