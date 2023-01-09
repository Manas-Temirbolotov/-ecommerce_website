from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from .models import Profile
from .serializers import IsSenderRegisterSerializer, IsBuyerRegisterSerializer


class IsSenderCreateProfileAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = IsSenderRegisterSerializer


class IsBuyerCreateProfileAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = IsBuyerRegisterSerializer


# class UserRegisterView(generics.CreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = IsSenderRegisterSerializer
