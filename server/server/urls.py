"""
URL configuration for server project.

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
from django.urls import include, path, re_path

import social_django.apps
from social_django.urls import urlpatterns as social_django_urls
from social_django.urls import app_name
import social_django

from gmod import views

urlpatterns = [
    path("", views.PageIndex, name="index"),
    path("players/", views.PagePlayers, name="players"),
    path("admin/", admin.site.urls),

    # Social Auth
    re_path(r"^", include((social_django_urls, app_name), namespace="social")),
]
