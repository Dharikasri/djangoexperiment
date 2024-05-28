from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Student, Marks
from .forms import StudentForm, MarksForm
from .serializers import StudentSerializer, MarksSerializer

# Function-based views for handling GET and POST requests
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        return render(request, 'student/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'GET':
        form = StudentForm()
        return render(request, 'student/add_student.html', {'form': form})
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

def enter_marks(request):
    if request.method == 'GET':
        form = MarksForm()
        return render(request, 'student/enter_marks.html', {'form': form})
    elif request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

# Class-based views with ModelViewSet to handle CRUD operations
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
