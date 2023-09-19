from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import place

# Create your views here.
def demo(request):
    obj=place.objects.all()
    return render(request,"index.html",{'results':obj})




