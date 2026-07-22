from rest_framework import serializers
from .models import Department, Employee, Instructor, SkillModule, Certification, ModuleSchedule

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SkillModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModule
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'