from django.urls import path,include
from .views import hello_view, SkillModuleListView, SkillModuleDetailView 
from .views import SkillModuleViewSet, EmployeeViewSet,CertificationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', SkillModuleViewSet, basename='course')
router.register('students', EmployeeViewSet, basename='student')
router.register('enrollments', CertificationViewSet, basename='enrollment')

urlpatterns = [
    path('hello/',hello_view,name='hello_view'),
    path('courses/', SkillModuleListView.as_view(), name='module-list'),
    path('courses/<int:pk>/',SkillModuleDetailView.as_view(),name='module-detail'),
    path('',include(router.urls))
]