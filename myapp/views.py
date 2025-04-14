from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm as user_form 
from . import forms, models
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'myapp/base.html', context = {})

@login_required
def home(request):
    all_task = models.Todo.objects.filter(user = request.user)
    return render(request, 'myapp/home.html', context = {'all_task': all_task})


def signup(request):
    if request.method == 'POST':
        user = user_form(request.POST)
        if user.is_valid():
            user.save()
            return redirect('login')
    else:
        user = user_form()
    return render(request, 'registration/signup.html', context = {'form': user})

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
    return render(request, 'myapp/tasks_form.html', context = {'form': form})

@login_required
def delete_task(request, id):
    todo = models.Todo.objects.get(user = request.user, id = id)
    todo.delete()
    return redirect('home')


@login_required
def update_task(request, id):
    todo = models.Todo.objects.get(user = request.user,  id = id)
    form = forms.TodoForm(instance=todo)

    if request.method == 'POST':
        form = forms.TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'myapp/update_task.html', {'form': form})