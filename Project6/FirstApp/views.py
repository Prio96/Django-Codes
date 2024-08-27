from django.shortcuts import render,redirect

from .models import Student
# Create your views here.
def home(request):
    student=Student.objects.all()
    print(student)
    return render(request,'home.html',{'data':student})

def delete_student(request,roll):
    Student.objects.get(pk=roll).delete()
    return redirect("homepage")
    
    
