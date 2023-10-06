from django.shortcuts import render
from rest_framework.status import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.response import Response
from .permissions import BookPermission
from app.models import Book,CustomUser
from .serializers import BookSerializer,CustomUserSerializer

@api_view(['GET','POST'])
@permission_classes([BookPermission])

def book(request):
    if request.method == 'GET':
        events = Book.objects.all()
        serializer = BookSerializer(events,many = True,context = {'request':request})
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data= request.data,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@permission_classes([IsAdminUser])

def custom_user(request):
    if request.method == 'GET':
        events = CustomUser.objects.all()
        serializer = CustomUserSerializer(events,many = True,context = {'request':request})
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CustomUserSerializer(data= request.data,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    