from django.urls import path
from .views import faculty_list, faculty_detail

urlpatterns = [
    path('', faculty_list, name='faculty_list'),
    path('<int:pk>/', faculty_detail, name='faculty_detail'),
]
