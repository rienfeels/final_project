# fsc_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StripingFormViewSet

router = DefaultRouter()
router.register(r'forms', StripingFormViewSet, basename='stripingform')

urlpatterns = [
    path('', include(router.urls)),
]
