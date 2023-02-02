"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from college.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('aboutus',about,name='about'),
    path('courses',courses,name='courses'),
    path('student',students_list,name='index'),
    path('departments',departments,name='departments'),
    path('departments/<int:department_id>/',department_details,name='department_details'),
    path('facillity',facillity,name='facillity'),
    path('facillity/<int:facillity_id>/',facillity_details,name='facillity_details'),
    path('contact_us',contact_us , name='contact_us'),


    #student class based views

     path(r'students/', StudentListView.as_view(), name='students'),
    path(r'add-student', StudentCreateView.as_view(),name='add-student'),
    path(r'edit-Student/<int:pk>/', StudentUpdateView.as_view() , name='edit-student'),
    path(r'Student/<int:pk>/', StudentDetailView.as_view() , name='view-student'),
]
