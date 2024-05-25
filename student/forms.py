from django import forms
from .models import Student
from .models import Marks

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'marks']