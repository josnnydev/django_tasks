 
from django.db import models
 
 
 
 

class Project(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name  

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()   
    done = models.BooleanField(default=False)
    project =  models.ForeignKey(Project, on_delete=models.CASCADE)  

    def __str__(self):
        return self.title + ' - ' + self.project.name  


 





     