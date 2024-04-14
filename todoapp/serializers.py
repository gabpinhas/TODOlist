from rest_framework import serializers
from .models import Task

#serializei os campos do book

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'