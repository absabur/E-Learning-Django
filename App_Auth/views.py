from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from App_Auth.forms import *
from App_Auth.models import *

# Create your views here.
def create_user(request):
    logout(request)
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Creation Successfull!")
            return redirect('home')
    return render(request, 'App_Auth/create_user.html', context={"form": form})


def login_page(request):
    logout(request)
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"Login successfull!")
                try:
                    if request.GET['next']:
                        return redirect(request.GET['next'])
                except Exception as e:
                    return HttpResponseRedirect(reverse('home'))
                
    return render(request, 'App_Auth/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,"Logout successfull!")
    return HttpResponseRedirect(reverse('home'))


@login_required
def userInfo(request):
    form = UserInfoForm()
    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,"User Info Added successfull!")
            return redirect('home')
    return render(request, 'App_Auth/userInfo.html', context={'form': form})


@login_required
def changeInfo(request, pk):
    user = User.objects.get(pk=pk)
    info = user.user_profile
    form = UserInfoChangeForm(instance=info)
    if request.method == 'POST':
        form = UserInfoChangeForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            messages.success(request,"User Info Updated successfull!")
            return redirect('home')
    return render(request, 'App_Auth/userInfo.html', context={'form': form, 'edit': True})