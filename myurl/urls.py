"""myurl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from mysite import views

myurlPatterns = [
    path('company/', views.company),
    path('sales/', views.sales),
    path('contact/', views.contact),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about/', views.about),
    path('about/<int:author_no>', views.about),
    path('info/', include(myurlPatterns)),
    path('mul/<int:x>/<int:y>/', views.mul),
    path('list/<int:yr>/<int:mon>/<int:day>/', views.listing, name='list-url'),
    path('F/<int:tem>/', views.temF, name='tempF-url'),
    path('C/<int:tem>/', views.temC, name='tempC-url'),
    path('post/<int:yr>/<int:mon>/<int:day>/<int:post_num>/', views.post, name='post-url'),
    path('post2/<int:yr>/<int:mon>/<int:day>/<int:post_num>/', views.post2, name='post-url-2'),
]

