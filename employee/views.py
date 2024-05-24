from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employee': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {'form': form})

def update_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return redirect('employee_list')  # or return a 404 page
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/update_employee.html', {'form': form})

def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return redirect('employee_list')  # or return a 404 page
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/delete_employee.html', {'employee': employee})

