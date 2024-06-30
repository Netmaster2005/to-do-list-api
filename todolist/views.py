from django.shortcuts import render
from django.views.generic import *
from .models import *

class TaskListView(ListView):
    model=Task
    template_name='home.html'