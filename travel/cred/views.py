from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass']
        confirmpass=request.POST['cpass']
        if password==confirmpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname, email=email)
                user.save();

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"reg.html")



