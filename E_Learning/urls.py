from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account/', include('App_Auth.urls')),
    path('student/', include('App_Student.urls')),
    path('teacher/', include('App_Teacher.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
