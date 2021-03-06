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
from bbs import views

urlpatterns = [
    re_path(r'^$',views.index),
    re_path(r'^category/(\d+)/$',views.category,name='category'),
    re_path(r'^detail/(\d+)/$',views.article_detail,name='article_detail'),
    re_path(r'^comment/$', views.post_comment, name='post_comment'),
    re_path(r'^comment_list/(\d+)/$', views.get_comments, name='get_comments'),
    re_path(r'^new_article/$', views.new_article, name='new-article'),
    re_path(r'^file_upload/$', views.file_upload, name='file_upload'),
    re_path(r'^latest_article_count/$', views.get_latest_article_count, name='get_latest_article_count'),

]
