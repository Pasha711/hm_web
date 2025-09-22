from django.urls import path
from . import views

urlpatterns = [
    # Головна сторінка визначена у корневому urls.py
    path('programs/', views.program_list, name='program_list'),
    path('programs/<int:pk>/', views.program_detail, name='program_detail'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
]
