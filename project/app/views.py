from django.shortcuts import render,redirect,get_object_or_404

from .models import Student
from django.contrib.messages import get_messages
from .forms import StudentForm
from django.contrib import messages
# Create your views here.
def home(request):
    object=Student.objects.all()
    print(object)
    return render(request, 'home.html',{'object':object})

def add_student(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
           # messages.add_message(request,messages.SUCCESS,"Congratulations")
            #messages.success(request,"Your Student info has been saved")
            messages.info(request,"login successfully")
            #it will help us to add retrieve messages outside template
            storage = get_messages(request)
            for message in storage:
                 print(message)
            return redirect('home')
    else:
        form=StudentForm()
    return render(request, 'addStudent.html',{'form':form})

def update_student(request,id):
    #print(f"Student ID: {id}")
    object=get_object_or_404(Student, id=id)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=object)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=StudentForm(instance=object)
    return render(request, 'updateStudent.html',{'form': form, 'id': id})

def delete_student(request,id):
    object=Student.objects.get(id=id)
    object.delete()
    return render(request,'delete.html')

