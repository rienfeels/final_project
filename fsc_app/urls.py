from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import MyModelViewSet, UserRegistrationView, CustomLoginView, CustomLogoutView, UserDetailsView, RegisterView

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('my_model/', MyModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user_register/', UserRegistrationView.as_view()),
    path('login/', CustomLoginView.as_view()),
    path('logout/', CustomLogoutView.as_view()),
    path('user_details/', UserDetailsView.as_view()),
    path('register/', RegisterView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]