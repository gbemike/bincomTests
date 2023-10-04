from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import *
from .forms import *

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    task_count = tasks.count()
    form = TaskForm()

    if request.method == 'POST':
        # this passes all the POST data into our form 
        form = TaskForm(request.POST)
        # checks if values are correct
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'tasks':tasks, 'task_count':task_count, 'form':form}
    return render(request, 'base/task.html', context)

def editTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        # this passes all the POST data into our form 
        form = TaskForm(request.POST, instance=task)
        # checks if values are correct
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'base/edit_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context={}
    return render(request, 'base/edit_task.html', context)