from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import taskform
from .models import task
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        all_tasks = task.objects.filter(user = user).order_by('-status')
        pendingTasks = task.objects.filter(status= 'P', user = user).count()
        context = {'pendingTasks' : pendingTasks, 'all_tasks' : all_tasks, 'user' : user}
        return render(request, 'home.html', context)

def loginUser(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, 'login.html', context)
    else:
        form = AuthenticationForm(data=request.POST)
        # print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form = AuthenticationForm()
            context = {
                "form": form
            }
            return render(request, 'login.html', context)

def registerUser(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form
        }
        print("abc")
        return render(request, 'register.html', context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        print("xyz")
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login') #redirect nhận vào tên path
        else:
            return render(request, 'register.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def addtaskpage(request):
    form = taskform()
    return render(request, 'addtaskpage.html', context={'form':form})

def addTask(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = taskform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('home')
        else:
            return render(request , 'home.html' , context={'form' : form})

def deleteTask(request, id):
    print(id)
    task.objects.get(pk = id).delete()
    return redirect('home')

def changeStatus(request, id, status):
    currentTask = task.objects.get(pk = id)
    currentTask.status = status
    currentTask.save()
    return redirect('home')

# def editTask(request, id):
