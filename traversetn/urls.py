"""traversetn URL Configuration

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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from traversetnapi.views import register_user, login_user
from traversetnapi.views import (TripView, RiverView, PlaceView, FavoriteView, MemberView) 

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'trips', TripView, 'trip')
router.register(r'rivers', RiverView, 'river')
router.register(r'places', PlaceView, 'place')
router.register(r'favorites', FavoriteView, 'favorite')
router.register(r'members', MemberView, 'member')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]
