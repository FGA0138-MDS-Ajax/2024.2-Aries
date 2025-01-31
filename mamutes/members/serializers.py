from rest_framework import serializers
from .models import Column, Task

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def get_responsible_names(self, obj):
        return [responsible.username for responsible in obj.responsible.all()]
