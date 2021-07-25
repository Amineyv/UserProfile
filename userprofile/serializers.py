from rest_framework import serializers, viewsets
from .models import *

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'


class DegreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Degree
        fields = '__all__'


class FieldStudySerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldStudy
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'
