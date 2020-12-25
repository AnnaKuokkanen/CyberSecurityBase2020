from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.
def register_user(request):
    user = User(username=request.POST['username'],
            password=request.POST['password'],
            firstname=request.POST['firstname'], 
            lastname=request.POST['lastname'],
            age=request.POST['age']
            )
    user.save()
    return render(request, 'registration.html')

@login_required
def home(request):
    return render(request, 'home.html')