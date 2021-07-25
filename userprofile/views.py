from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from userprofile.models import *
from rest_framework.views import APIView
from rest_framework import  viewsets
from .serializers import *

class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    http_method_names = ['get', 'post', 'put']

class DegreeView(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    http_method_names = ['get', 'post', 'put']

class FieldStudyView(viewsets.ModelViewSet):
    queryset = FieldStudy.objects.all()
    serializer_class = FieldStudySerializer
    http_method_names = ['get', 'post', 'put']


class EducationView(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer