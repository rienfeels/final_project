"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# final_project/urls.py
from django import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fsc_app.views import MyModelViewSet, UserRegistrationView  # Import the viewset from your app

from django.contrib.auth.views import LoginView  # Import the LoginView class

router = DefaultRouter()
router.register(r'forms', MyModelViewSet, basename='stripingform')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include the auth app's urls
    path('api/', include(router.urls)),  # Include the app's viewset directly
    # path('register/', UserRegistrationView.as_view(), name='user-registration'),  # Add the registration view
    path('login/', LoginView.as_view(), name='user-login'),
    path("register/", UserRegistrationView.as_view(), name="user_register"),
    
]
