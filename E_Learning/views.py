from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.http import HttpResponse
from App_Auth.models import *

# View for the home page
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('App_Auth:login'))        
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        return HttpResponseRedirect(reverse('App_Auth:userInfo'))
    return HttpResponseRedirect(reverse('App_Teacher:articles'))


