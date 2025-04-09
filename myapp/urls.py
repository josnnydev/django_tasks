from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.index,name='index'  ),
    path('about', views.about, name='about'  ),

    
    path('projects', views.projects, name='projects'  ),
     
     
    path('create_task', views.create_task, name='create_task'  ),
    path('create_projects', views.create_projects, name='create_projects'  ),
    path('project/<int:id>', views.project_detail, name='project_detail'  ),
    
    
    path('delete_task/<int:id>', views.delete_task, name='delete_task'  ),
    path('update_task/<int:id>', views.update_task, name='update_task'  ),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),

]