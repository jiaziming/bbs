"""s20bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path,include
from webchat import views

urlpatterns = [

    re_path(r'^$', views.dashboard, name='chart_dashboard'),
    re_path(r'^msg_send/$', views.send_msg, name='send_msg'),
    re_path(r'^new_msg/$',views.get_new_msgs,name ='get_new_msgs'),
    re_path(r'^file_upload/$', views.file_upload,name='file_upload'),
    re_path(r'^file_upload_progress/$', views.file_upload_progress, name='file_upload_progress'),
    re_path(r'^delete_cache_key/$', views.delete_cache_key, name='delete_cache_key'),

]
