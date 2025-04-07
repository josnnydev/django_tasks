from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, JsonResponse
from myapp.forms import CreateTaskForm,CreateProjectForm 
from myapp.models import Project, Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
 
 
def index(request):
    return render(request, 'index.html',status=200 )

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   
            return redirect('create_task')
        else:
            return render(request, 'signup/signup.html', {
                'form': form,
                'error': 'Please correct the errors below.'
            })
    else:
        form = UserCreationForm()

    return render(request, 'signup/signup.html', {'form': form})
  
     


def about(request):
    return render(request, 'about.html',status=200 ) 

def projects(request):
    projects =Project.objects.all()
    
     
    return render(request,'projects/projects.html', {'projects': projects}) 

def tasks(request):
    tasks = Task.objects.all()
    
    return render(request,'tasks/tasks.html', {'tasks': tasks})    


def task(request, id):
    if not Task.objects.filter(id=id).exists():
        return get_object_or_404(Task, id=id)
    else:    
        task = Task.objects.get(id=id)
        return JsonResponse(task.title,safe=False,status=200 )    

def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('tasks')
    else:
        form = CreateTaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def create_projects(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('projects')
    else:
        form = CreateProjectForm()
    return render(request, 'projects/create_projects.html', {'form': form})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project__id=id)
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    response = HttpResponse(status=200)
    response['HX-Redirect'] = '/tasks'   
    return response


