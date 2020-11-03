from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect    
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from HospitalApp.forms import *
from .models import * 
from  django.http import HttpResponse

# Create your views here.
"""
def About(request):
    return render(request,'about.html')
"""

def Contact(request):
    return render(request,'contact.html')

 
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')



def Login(request):
    error=""
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)      
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
        context={'error':error}

        if user not in is_staff:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username or Password Invalid')
    context={}
    return render(request,'login.html',context)
"""

def LoginPage(request):
    form=LoginForm()
    if request.method=="POST":
        username=request.POST('username')
        password=request.POST('password')
        user=authenticate(request,username=username,password=password)

        #form=LoginForm(request.POST)
        if user is not None:
            login(request,user)
            return redirect('contact')
        else:
            messages.info(request,' Invalid credentials please provide valid credentials')

            #return redirect('/contact')

    context={}
    return render(request,'login.html',context)
"""

def LogOut(request):
    if not request.user.is_staff:
        return redirect('login')
    #logout(request)
    return HttpResponseRedirect('/thank')

def Thank(request):
    return HttpResponse("<h1>Thanks for visiting the Apollo Hosptital</h1>")


def View_Doctor(request):
    #if user is not None:
    if not request.user.is_staff:
        #login(request,user)
        return redirect('login')
    doc = Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)



def Add_Doctor(request):

    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n=request.POST['name']
        c=request.POST['contact']
        sp=request.POST['special']
        #user = authenticate(request,name=name,contact=contact,special=special)      
        try:
            Doctor.objects.create(name=n,mobile=m,spicialization=sp)

            error="no"      
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_doctor.html',d)


def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

