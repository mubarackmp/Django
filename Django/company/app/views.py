from django.shortcuts import render
from app.models import *
from app.form import *

# Create your views here.

def add(request):
    a=Employeform()
    if request.method=='POST':
        a=Employeform(request.POST)
        if a.is_valid():
            a.save()
            return home(request)
    return render(request,'lists.html',{'f':a})

def form1(request):
    if request.method=='POST':
        na=request.POST.get('n')
        roll=request.POST.get('rl')
        pl=request.POST.get('p')
        data=Employ.objects.create(name=na,rollno=roll,place=pl)
        data.save()
        return home(request)
    return render(request,'lists.html')
    

def deleete(request,p):
    a=Employ.objects.get(pk=p)
    a.delete()
    return home(request)

def deleetee(request,q):
    a=Employ.objects.get(pk=q)
    a.delete()
    return home(request)

def edit(request,p):
    a=Employ.objects.get(pk=p)
    b=Employform(instance=a)
    if request.method=='POST':
        b=Employform(request.POST,instance=a)
        if b.is_valid():
            b.save()
            return home(request)
    return render(request,'lists.html',{'z':b})
    
def editee(request,q):
    a=Employee.objects.get(pk=q)
    b=Employeform(instance=a)
    if request.method=='POST':
        b=Employeform(request.POST,instance=a)
        if b.is_valid():
            b.save()
            return home(request)
    return render(request,'lists.html',{'f':b})

def home(request):
    b=Employee.objects.all()
    e=Employ.objects.all()
    return render(request,'lists.html',{'c':b,'g':e}) 