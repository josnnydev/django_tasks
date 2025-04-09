 
from django import forms
from .models import  Task, Project 
from django.contrib.auth.models import User 
 


class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    done = forms.BooleanField(required=False)
    project = forms.ModelChoiceField(queryset=Project.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'done', 'project']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # usa .pop() con valor por defecto
        super().__init__(*args, **kwargs)
        if user:
            self.fields['project'].queryset = Project.objects.filter(user=user)



class CreateProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    user = forms.ModelChoiceField(queryset=User.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Project
        fields = ['name']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # usa .pop() con valor por defecto
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].queryset = User.objects.filter(id=user.id)
            self.fields['user'].initial = user



  


 

 

 


    
