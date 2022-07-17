"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from TrackJob.views import home_view,register_view,login_view,showrecord_view,job_detail_view,job_add_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home_view, name = 'home'),
    path('login/',login_view),
    path('register/',register_view),
    path('showrecord/',showrecord_view),
    path('jobdetial/',job_detail_view),
    path('jobadd/',job_add_view),




]
