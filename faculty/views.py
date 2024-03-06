from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Faculty

def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty/faculty_list.html', {'faculties': faculties})

def faculty_detail(request, pk):
    faculty = Faculty.objects.get(pk=pk)
    return render(request, 'faculty/faculty_detail.html', {'faculty': faculty})
