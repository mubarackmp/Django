from django.shortcuts import render

from app1.models import *
from app1.form import userform1

# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    d=userform1()
    if request.method=='POST':
        d=userform1(request.POST)
        if d.is_valid():
            d.save()
            return lists(request)
    
    return render(request,'signup.html',{'form':d})
        
def lists(request):
    p=users.objects.all()
    return render(request,'list.html',{'d':p})

def home(request):
    return render(request,'home.html')