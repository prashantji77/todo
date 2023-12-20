from ast import Delete, Return
from threading import stack_size
from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from todoAPI.models import product
from todoAPI.serializers import product_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

ADMIN_HTTP_METHODS=["POST","PUT","DELETE","PATCH"]

class TodoPermissions(BasePermission):  # this is permission class 
    def has_permission(self, request, view):
        if request.user.is_authenticated :
            if request.method in SAFE_METHODS:
                return True
            if request.method in ADMIN_HTTP_METHODS and request.user.is_admin:
                return True
        return False


class todoList(APIView):
    
    permission_classes=[TodoPermissions]
    
    def get(self,request,format=True): # this function is used to get all element  
        item=product.objects.all()
        serializer=product_serializer(item,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=True): # this function is used to create new element 
        serializer=product_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
class todoItem(APIView):
    permission_classes=[TodoPermissions]
    
    def myFunction(self,pk):  # this is function which is used for to get object by using id
        try:
            return product.objects.get(pk=pk)
        except product.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=True): #this is used for the get element by using id
        list1=self.myFunction(pk) # here  have myFunction to get element by using by id
        serializer=product_serializer(list1) # this is serializer where we can get all elemnt 
        return Response(serializer.data) # here we return the serializer data 
    
    def put(self,request,pk,format=True):# this function is used to update by usnin id
        list1=self.myFunction(pk)
        serializer=product_serializer(list1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.data,
                        status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk): #this function is used to delete item by using id
        list1=self.myFunction(pk)
        list1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
