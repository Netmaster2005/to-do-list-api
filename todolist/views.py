from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import action
class ListTodo(generics.ListAPIView):
    queryset=Task.objects.all()
    serializer_class=ToDoSerializer
    filter_backends=(SearchFilter, OrderingFilter)
    search_fields=('Title', 'Due_Date', 'Description')

class CreateTodo(generics.CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=ToDoSerializer 

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=ToDoSerializer
