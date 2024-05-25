from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)


    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.marks}"
