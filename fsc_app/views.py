# fsc_app/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import StripingForm
from .serializers import StripingFormSerializer
# from .views import StripingFormViewSet

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = StripingForm.objects.all()
    serializer_class = StripingFormSerializer
    permission_classes = [IsAuthenticated]
