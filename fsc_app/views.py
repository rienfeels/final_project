from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import DailyReport, Project
from .serializers import DailyReportSerializer, UserSerializer
from rest_framework import generics

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer
    permission_classes = [IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return Response({"message": "Login successful", "user": self.request.user.username}, status=status.HTTP_200_OK)

class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        self.logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    
class DailyReportViewSet(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer