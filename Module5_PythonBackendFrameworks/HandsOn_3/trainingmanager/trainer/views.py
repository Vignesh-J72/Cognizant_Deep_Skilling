from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import SkillModule, Employee, Certification
from .serializers import SkillModuleSerializer, EmployeeSerializer, CertificationSerializer
from rest_framework import viewsets
from rest_framework.decorators import action


def hello_view(request):
    return HttpResponse("Training manager is running.")

class SkillModuleListView(APIView):
    def get(self, request):
        modules=SkillModule.objects.all()
        serializer=SkillModuleSerializer(modules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer=SkillModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillModuleDetailView(APIView):
    def get(self, request, pk):
        module=get_object_or_404(SkillModule, pk=pk)
        serializer=SkillModuleSerializer(module)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        module=get_object_or_404(SkillModule, pk=pk)
        serializer=SkillModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        module=get_object_or_404(SkillModule, pk=pk)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class SkillModuleViewSet(viewsets.ModelViewSet):
    queryset = SkillModule.objects.all()
    serializer_class = SkillModuleSerializer

    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        module = self.get_object()
        # Find all employees who have a certification record for this module
        certified_employees = Employee.objects.filter(certifications__skill_module=module)
        serializer = EmployeeSerializer(certified_employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer