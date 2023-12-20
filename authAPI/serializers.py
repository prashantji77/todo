from django.db import models
from authAPI.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext as _
from rest_framework.validators import UniqueValidator
from authAPI.models import User
from rest_framework import serializers



class UserSerializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=256)
    last_name=serializers.CharField(max_length=256)
    email=serializers.EmailField(max_length=100,validators=[UniqueValidator(queryset=User.objects.all())])
    role=serializers.CharField(max_length=256)
    password=serializers.CharField(max_length=100,write_only=True)

    def create(self,validate_data):
        password=validate_data.pop("password")
        if validate_data.get('role')=='admin':
            validate_data['is_admin']=True
        user=User.objects.create(**validate_data)
        user.set_password(password)
        user.save()
        return validate_data