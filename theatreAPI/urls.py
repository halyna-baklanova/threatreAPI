"""
URL configuration for theatreAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.authtoken import views

from user.views import CreateUserView, LoginUserView, ManageUserView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("theatre/", include("theatre.urls", namespace="theatre")),
    path("user/register/", CreateUserView.as_view(), name="user-create"),
    path("user/login/", LoginUserView.as_view(), name="token"),
    # path("user/login/", LoginUserView.as_view(), name="user-login"),
    path("user/me/", ManageUserView.as_view(), name="user-manage"),
]
