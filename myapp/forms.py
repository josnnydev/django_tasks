 
from django import forms
from .models import  Task, Project
 


class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    done = forms.BooleanField(required=False)
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'done', 'project']



class CreateProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Project
        fields = ['name']


 

 

 


    
