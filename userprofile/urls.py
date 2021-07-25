from django.urls import path, include 
from django.conf.urls import url
from rest_framework import routers 
from . import views
from .views import *

app_name = "profile"

router = routers.DefaultRouter()                      
router.register(r'school', views.SchoolView, basename='school')
router.register(r'degree', views.DegreeView, basename='degree')
router.register(r'fieldstudy', views.FieldStudyView, basename='fieldstudy')
router.register(r'education', views.EducationView, basename='education')
router.register(r'userprofile', UserProfileView, basename='userprofile')

urlpatterns = [
	path('', include(router.urls)),
]
