from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.

tasks = ["Task 1", "Task 2", "Task 3"]

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm
    })