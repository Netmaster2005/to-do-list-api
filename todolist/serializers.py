from rest_framework import serializers
from .models import *

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('id','Title','Description','Due_Date','Completed')