
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home , name ='home'),
    path('Login/', views.login, name = 'login'),
    path('signup/', views.signup),
    path('thanks/', views.thanks,name = 'thanks'),
    path('add-todo/', views.todo,name = 'to-do'),
    path('delete-todo/<int:id>', views.delete_todo),
    path('logout/', views.signout)

]