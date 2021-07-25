from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.transaction import Atomic, get_connection
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django_jalali.db import models as jmodels
import datetime


class School(models.Model):
    schools = models.CharField(max_length=300, blank=True, verbose_name='School Category',)

    def __str__(self):
        return self.schools


class Degree(models.Model):
    degree = models.CharField(max_length=300, blank=True, verbose_name='Degree',)

    def __str__(self):
        return self.degree


class FieldStudy(models.Model):
    fieldStudy = models.CharField(max_length=300, blank=True, verbose_name='Field Study',)

    def __str__(self):
        return self.fieldStudy


class Education(models.Model):
    school = models.ForeignKey('School', related_name='schoo', on_delete=models.CASCADE)
    degree = models.ForeignKey('Degree', related_name='degre', on_delete=models.CASCADE)
    fieldStudy = models.ForeignKey('FieldStudy', related_name='Study', on_delete=models.CASCADE)
    userprofile = models.ForeignKey('UserProfile', related_name='profil', on_delete=models.CASCADE, null=True,blank=True)
    startDate = jmodels.jDateField(verbose_name='Start Date') 
    endDate = jmodels.jDateField(verbose_name='End Date') 
    grade = models.CharField(max_length=200, blank=True, verbose_name='Grade',)    
    activitiesSocieties = models.CharField(max_length=200, blank=True, verbose_name='Activities and Societies',)    
    description = models.TextField(default='', blank=True, verbose_name='Description')


class UserProfile(models.Model):
    first_name = models.CharField(max_length=36, verbose_name='First Name')
    last_name = models.CharField(max_length=48, verbose_name='Last Name')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Profile Picture')

    def __str__(self):
        full_name = self.first_name + ' - ' + self.last_name
        return full_name
