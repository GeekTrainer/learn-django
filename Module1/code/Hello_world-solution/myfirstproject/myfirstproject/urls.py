"""myfirstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# [TODO]: Add the include function to the list of imports from django.urls
from django.urls import include, path

urlpatterns = [
    # [TODO]: Add the code to create the URLconf for the app
    path('hello_world/', include('hello_world.urls')),
    path('admin/', admin.site.urls),
    
]
