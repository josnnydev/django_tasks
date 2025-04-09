from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse 
from myapp.forms import CreateTaskForm,CreateProjectForm 
from myapp.models import Project, Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html',status=200 )

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)   
#             return redirect('create_task')
#         else:
#             return render(request, 'signup/signup.html', {
#                 'form': form,
#                 'error': 'Please correct the errors below.'
#             })
#     else:
#         form = UserCreationForm()

#     return render(request, 'signup/signup.html', {'form': form})

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('create_task')
            except IntegrityError:
                return render(request, 'signup/signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup/signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('create_task')
        else:
            return render(request, 'signin/signin.html', {'form': form, 'error': 'User not found, Please Signup .'})
    else:
        form = AuthenticationForm()

    return render(request, 'signin/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('index')
  
     


def about(request):
    return render(request, 'about.html',status=200 ) 

@login_required
def projects(request):
    projects =Project.objects.filter(user=request.user)
    
    
     
    return render(request,'projects/projects.html', {'projects': projects}) 

    


@login_required
def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, user=request.user)  # ✅ Agrega 'user' aquí también
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('projects')
    else:
        form = CreateTaskForm(user=request.user)  # Esto ya estaba bien
    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def create_projects(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST, user=request.user)  # ✅ Aquí también
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('projects')
    else:
        form = CreateProjectForm(user=request.user)  # Esto está bien
    return render(request, 'projects/create_projects.html', {'form': form})

@login_required
def project_detail(request, id):
    project = get_object_or_404(Project, id=id,user=request.user)
    tasks = Task.objects.filter(project__id=id,user=request.user)
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})

 
@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id,user=request.user)
    task.delete()
    response = HttpResponse(status=200)
    response['HX-Redirect'] = '/projects'    
    return response

@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
         
        form = CreateTaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            response = HttpResponse(status=200)
            response['HX-Redirect'] = '/project/' + str(task.project.id)  
            return response
    else:
        form = CreateTaskForm(instance=task, user=request.user)

    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})


 



