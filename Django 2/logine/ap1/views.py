from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render (request,'base.html')


def signp(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password')
        password2=request.POST.get('confirm')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already exists !!!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect(login_user)
        else:
            print('wrong password')
    return render (request,'signup.html')

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        password1=request.POST.get('password')
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(login_user)
    return render(request,'login.html')

    
    


def logoute(request):
    logout(request)
    return redirect(login_user)