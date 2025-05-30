"""
URL configuration for django_menu_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from menuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('base/',views.base,name='base'),
    path('funk/', views.funk, name='funk'),
    path('funk2/',views.funk2, name='fun2')
]


