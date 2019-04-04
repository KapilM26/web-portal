"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cil'

urlpatterns = [
    #path('', views.Index.as_view(), name='index'),
    path(views.LogIn.as_view(), name='login'),
    path('adminauth/', views.AdminAuth.as_view(), name='adminauth'),
    path('guestauth/', views.GuestAuth.as_view(), name='guestauth'),
    path('guestadd/', views.GuestAdd.as_view(), name='guestadd'),
    path('guestedit/', views.GuestEdit.as_view(), name='guestedit'),
    path('guestupdate/?<int:profile>/', views.GuestUpdate.as_view(), name='guestupdate'),
    path('guestdelete/', views.GuestDelete.as_view(), name='guestdelete'),
    path('logout/', views.logoff, name='logout'),
    path('logs/', views.LogView.as_view(), name='logs'),
    path('admin/logout/', views.logoff, name='adminlogout')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
