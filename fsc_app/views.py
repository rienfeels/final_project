# fsc_app/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.views import LoginView
from .models import DailyReport, Project
from .serializers import StripingFormSerializer, UserSerializer
from rest_framework import generics
# from .views import StripingFormViewSet

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all()
    serializer_class = StripingFormSerializer
    permission_classes = [IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED, headers=headers)
    
class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return Response({"message": "Login successful", "user": UserSerializer(self.request.user).data}, status=status.HTTP_200_OK)
    
class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        self.logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


