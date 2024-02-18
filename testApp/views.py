from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.shortcuts import get_object_or_404, redirect


def home(request):
    qs = Student.objects.all()
    return render(request, 'testApp/home.html',{'qs':qs})

def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data added successfully")
    return render(request, 'testApp/create.html', {'form':form})

def update_student(request, pk):
    isinstance = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=isinstance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse("Updated Successfully")
    return render(request, 'testApp/update.html', {'form':form})

def delete_student(request, pk):
    qs = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        qs.delete()
        return HttpResponse("Data Deleted")
    context = {}
    return render(request, 'testApp/destroy.html')