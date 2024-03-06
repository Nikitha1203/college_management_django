from django.urls import path
from .views import student_list, student_detail

urlpatterns = [
    path('', student_list, name='student_list'),
    path('<int:pk>/', student_detail, name='student_detail'),
]
