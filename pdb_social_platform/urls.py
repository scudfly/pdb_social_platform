"""
URL configuration for pdb_social_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from login.views import login, userlogin, register, userregister
from main.views import index, post, postContent, trend, focus

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login, name="login"),
    path("", index, name="index"),
    path("userlogin/", userlogin, name="userlogin"),
    path("register/", register, name="register"),
    path("userregister/", userregister, name="userregister"),
    path("post/", post, name="userregister"),
    path("postContent/", postContent, name="postContent"),
    path("trend/", trend, name="trend"),
    path("focus/", focus, name="focus"),
]
