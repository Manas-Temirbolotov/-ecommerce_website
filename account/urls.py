from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/sender/', views.IsSenderCreateProfileAPIView.as_view()),
    path('api/account/register/buyer/', views.IsBuyerCreateProfileAPIView.as_view()),
    path('token/', obtain_auth_token),
]