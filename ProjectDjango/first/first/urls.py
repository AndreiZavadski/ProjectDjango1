"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from helloworld.views import seasons
from helloworld.views import winter
from helloworld.views import spring
from helloworld.views import summer
from helloworld.views import autumn

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seasons/', seasons),
    path('seasons/winter/', winter),
    path('seasons/spring/', spring),
    path('seasons/summer/', summer),
    path('seasons/autumn/', autumn)
]
