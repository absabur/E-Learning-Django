from django.urls import path
from App_Auth.views import *

app_name = 'App_Auth'

urlpatterns = [
    path('signup/', create_user, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user-info/', userInfo, name='userInfo'),
    path('change-info/<pk>/', changeInfo, name='changeInfo'),
]
