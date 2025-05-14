"""
URL configuration for csa_testing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('buttons/', views.buttons_page, name='buttons_page'),
    path('sql/', views.sql, name='sql_doc'),
    path('fishing/', views.fishing_page_doc, name='fishing_doc'),
    path('fishing/test', views.fishing_page_test, name='fishing_page_test'),
    path('fishing/result', views.fishing_result, name='fishing_result'),
    path('sql/login', views.login_sql, name='login_sql'),
    path('xss/', views.xss_page, name='xss_doc'),
    path('xss/test', views.xss_page_test, name='xss_demo_page'),
    path('ddos', views.ddos_page, name='ddos_doc'),

]