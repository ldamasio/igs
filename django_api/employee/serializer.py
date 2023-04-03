from django.db.models import fields
from rest_framework import serializers
from .models import Employee, Department
  
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')

    def to_representation(self, instance):
        rep = super(EmployeeSerializer, self).to_representation(instance)
        rep['department'] = instance.department.name
        return rep

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)

