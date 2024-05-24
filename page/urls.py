from django.urls import path
from . import views

urlpatterns = [
    path('pageone/', views.first_page, name='first_page'),
    path('pagetwo/', views.second_page, name='second_page'),
    
]
