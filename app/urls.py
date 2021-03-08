from django.urls import path
from . import views

# app_name = 'user'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser),
    path('logout/', views.logoutUser),
    path('addTask/', views.addTask),
    path('deleteTask/<int:id>', views.deleteTask),
]