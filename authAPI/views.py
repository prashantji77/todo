from django.shortcuts import render
from authAPI.models import User
from authAPI.serializers import UserSerializer
from rest_framework.viewsets import ViewSet
from rest_framework import status 
from rest_framework.response import Response



# Create your views here.

class UserApiViewSet(ViewSet): # this class is used to create user
    serializer_class=UserSerializer 
    def create(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)
        
