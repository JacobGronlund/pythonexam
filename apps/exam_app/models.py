from __future__ import unicode_literals
from django.db import models
import time
import datetime
from datetime import datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'First name must have more than two characters'
        if len(postData['username']) < 3:
            errors['username'] = 'Username must have more than two characters'
        if postData['password'] != postData['password_conf']:
            errors['password'] = 'Passwords need to match'
        if len(postData['password']) < 8:
            errors['password'] = 'Password needs to be at least 8 characters'
        return errors

class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['destination']) < 1:
            errors['destination'] = 'No empty entries'
        if len(postData['desc']) < 1:
            errors['desc'] = 'No empty entries'
        if len(postData['datefrom']) < 1:
            errors['datefrom'] = 'No empty entries'
        if len(postData['dateto']) < 1:
            errors['dateto'] = 'No empty entries'
        #if postData['datefrom'] < datetime.now():
            #triperrors['datefrom'] = 'date cannot be in the past'
        #if postData['dateto'] > postData['datefrom']:
            #errors['dateto'] = 'date to has to be after date from'
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    datefrom = models.DateField()
    dateto = models.DateField()
    objects = TripManager()

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    planned_trips = models.ManyToManyField(Trip, related_name = "users")
    objects = UserManager()


    
