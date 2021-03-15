from django.urls import path
from . import views

# app_name = 'user'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser),
    path('logout/', views.logoutUser),
    path('addTask/', views.addTask),
    path('addtaskpage/', views.addtaskpage),
    path('deleteTask/<int:id>', views.deleteTask),
    path('change-status/<int:id>/<str:status>/', views.changeStatus),
    # path('editTask/<int:id>', views.editTask),
]