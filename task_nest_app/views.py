from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm as user_form 
from . import forms, models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.



def index(request):
    return render(request, 'task_nest_app/base.html', context = {})



@login_required
def home(request):
    tasks = models.Todo_model.objects.filter(user = request.user)
    return render(request, 'task_nest_app/home.html', context = {'all_task': tasks})


def signup(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            user = form.save()
            #Auto Login
            login(request, user)
            return redirect('home')
    else:
        form = user_form()
    return render(request, 'registration/signup.html', context = {'form': form})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = forms.TodoForm(request.POST)
        if form.is_valid():
            task = form.save(commit = False)
            task.user = request.user 
            task.save()
            return redirect('home')
    else:
        form = forms.TodoForm()
    return render(request, 'task_nest_app/task_form.html', context = {'form': form})

@login_required
def delete_task(request, id):
    todo = models.Todo_model.objects.get(user = request.user, id = id)
    todo.delete()
    return redirect('home')


@login_required
def update_task(request, id):
    todo = models.Todo_model.objects.get(user = request.user,  id = id)
    form = forms.TodoForm(instance=todo)

    if request.method == 'POST':
        form = forms.TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'task_nest_app/update_task.html', {'form': form})