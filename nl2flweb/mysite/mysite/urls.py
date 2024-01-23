"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from blog.views import solveform, file2nlreq
from blog.views.register import RegisterView

urlpatterns = [
    path('nl2ltl/',
         auth_views.LoginView.as_view(template_name='blog/nl2ltl.html'),
         name='nl2ltl'),
    path('hello/', solveform.hello, name='hello3'),
    path('postnl/', solveform.postnl),
    path('filesolve/', file2nlreq.filesolve),
    path('computesim/', file2nlreq.computesim),
    path('postflimg/', solveform.postflimg),
    path('enviar/',
         auth_views.LoginView.as_view(template_name='blog/enviar.php'),
         name='enviar'),
    path('', include('django.contrib.auth.urls'))
]
