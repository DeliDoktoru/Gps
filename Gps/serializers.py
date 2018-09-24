from rest_framework import serializers
from .models import Employee,Employer

class EmployeeSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields='__all__'
class EmployerSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields='__all__'