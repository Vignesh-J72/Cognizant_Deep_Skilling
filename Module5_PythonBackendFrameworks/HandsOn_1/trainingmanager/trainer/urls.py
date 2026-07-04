from django.urls import path
from .views import hello_view

urlpatterns = [
    path('main/',hello_view,name='placeholder')
]