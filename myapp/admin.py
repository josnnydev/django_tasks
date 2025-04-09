from django.contrib import admin
from .models import Project, Task 

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')
     

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task) 
 

 


 
      

