from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

#search filter Model
from .filter import SearchFilter

#restrictions on users
from django.contrib.auth.decorators import login_required


from .models import *
from .form import TaskForm, NewUserForm


#filter users

def user_auth(request):
    check_auth = Task.objects.filter(user = request.user)
    return render(request, 'base/task_list.html', {'check_auth':check_auth}) 

# Create your views here.
@login_required(login_url = 'login')
def task_list(request):

    tasks = Task.objects.filter(user = request.user)


    #TODO: Fix search filter
    searchFilter = SearchFilter(request.GET, queryset = tasks)

    tasks = searchFilter.qs

    context = {'tasks': tasks, 'searchFilter':searchFilter}

    return render(request, 'base/task_list.html', context)

@login_required(login_url = 'login')
def task_detail(request, pk):

    tasks = Task.objects.get(id=pk)

    context = {'tasks': tasks}
    
    return render(request, 'base/task_detail.html', context)

@login_required(login_url = 'login')
def create_new_task(request): 
    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)
        
        if form.is_valid():
        
            form.save()

            return redirect('/')

    context = {'form': form}
    
    return render(request, 'base/task_create.html', context)

@login_required(login_url = 'login')
def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
        
            form.save()
        
            return redirect('/')

    context = {'form': form}
    return render(request, 'base/task_create.html', context)

@login_required(login_url = 'login')
def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()

        return redirect('/')

    context = {'task': task}

    return render(request, 'base/confirm_delete_task.html', context)

#TODO: add registration page

def user_login(request):
    if request.method == 'POST':
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():

            user_username = request.POST.get('username')
            pass_username = request.POST.get('password')

            user = authenticate(username=user_username, password=pass_username)

            if user is not None:
                login(request, user)
    
                return redirect('home')

    form = AuthenticationForm()

    context = {'form':form}

    return render(request, 'base/login.html',context)

def user_register(request):
    
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('new user created')
            return redirect('home')

    context = {'form':form}
    
    return render(request,'base/register.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')

