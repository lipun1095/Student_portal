"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views


urlpatterns = [
    path('student_list/', views.show_student_list, name='student_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:roll_no>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:roll_no>/', views.delete_student, name='delete_student'),
    path('add_student_mark/', views.add_student_mark, name='add_student_mark'),# This IS Not Used.
    path('view_mark/<int:roll_no>/', views.show_student_mark, name='view_mark'),
    path('', views.welcome_view, name='welcome_view'),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view, name='signup'),
]
