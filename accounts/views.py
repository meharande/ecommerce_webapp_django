from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection
import json, pickle

from accounts.forms import UserRegisterForm

from .forms import UserLoginForm

User = get_user_model()

# Create your views here.
def registration_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.userbiometicedetails.aadhar = form.cleaned_data.get('aadhar_no')
        user.save()
        login(request, user)
        form = UserRegisterForm()
    return render(request, 'register.html', context={'form': form})

def login_view(request):
    form = UserLoginForm(request.POST or None)
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        authenticated_user = authenticate(request, username=username, password=password)
        print(username, password, authenticated_user)
    except Exception as e:
        raise e
    if authenticated_user is not None:
        print('Entetred if ')
        login(request, authenticated_user)
        print('after login')
        print(request)
        return redirect('profile')


    return render(request, 'login.html', context={"form":form})

@login_required
def profile_view(request):
    return render(request, 'profile.html', context={})

def logout_view(request):
    logout(request)
    return redirect('login')