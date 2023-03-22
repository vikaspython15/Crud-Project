from django.urls import path
from django.shortcuts import render, redirect
from .forms import Employee, EmployeeForm


def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/crud/read/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'CRUD/Creater.html', {'form': form})


def read(request):
    employees = Employee.objects.all()
    return render(request, "CRUD/ReadDelete.html", {'employees': employees})


def update(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            print("update")
            return redirect("/crud/read/")
    
    return render(request, 'CRUD/Update.html', {'employee': employee})


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/crud/read/")


urlpatterns = [
    path('',  read),
    path('create/', create),  # C
    path('read/', read),  # R
    path('update/<int:id>', update),  # U
    path('delete/<int:id>', delete),  # D
]
