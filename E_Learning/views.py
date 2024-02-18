from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from App_Auth.models import *
from django.contrib import messages


# View for the home page
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('App_Auth:login'))
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information!")
        return HttpResponseRedirect(reverse('App_Auth:userInfo'))
    return HttpResponseRedirect(reverse('App_Teacher:articles'))


