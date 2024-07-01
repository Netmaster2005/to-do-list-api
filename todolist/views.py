from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class ListTodo(generics.ListAPIView):
    queryset=Task.objects.all()
    serializer_class=ToDoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=ToDoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=ToDoSerializer
