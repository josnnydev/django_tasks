 
from django.db import models
from django.contrib.auth.models import User

 
 
 
 

class Project(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='projects') 
     
    
    def __str__(self):
        return self.name + ' - ' + self.user.username  

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()   
    done = models.BooleanField(default=False)
     
    project =  models.ForeignKey(Project, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tasks') 
    

    def __str__(self):
        return self.title + ' - ' + self.project.name + ' - ' + self.user.username  


 





     