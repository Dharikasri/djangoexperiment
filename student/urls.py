from django.urls import path
from . import views
from .views import StudentViewSet, MarksViewSet

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('enter_marks/', views.enter_marks, name='enter_marks'),
    path('students/', StudentViewSet.as_view, name='student-list'),
    path('marks/', MarksViewSet.as_view, name='marks-list'),
]
