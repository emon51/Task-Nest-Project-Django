from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.signup, name = 'signup'),  
    path('home/', views.home, name = 'home'), 
    path('add_task/', views.add_task, name = 'add_task'), 
    path('delete_task/<int:id>', views.delete_task, name = 'delete_task'), 
    path('update_task/<int:id>', views.update_task, name = 'update_task'), 
]