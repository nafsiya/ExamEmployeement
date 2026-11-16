from rest_framework import serializers
from employeeApp.models import EmpolyeeModel,TaskModel

class EmployeeSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=EmpolyeeModel
        fields="__all__"
        
        read_only_fields=["joining_date"]
    

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskModel
        fields="__all__"
        
        read_only_fields=["assigned_to","id"]
        