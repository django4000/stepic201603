"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','qa.views.test', name='root' ),
    url(r'^login/','qa.views.test', name='login' ),
    url(r'^signup/','qa.views.test', name='signup' ),
    url(r'^ask/','qa.views.test', name='ask_index' ),
    url(r'^new/','qa.views.test', name='ask_new' ),
    url(r'^popular/','qa.views.test', name='login' ),
    url(r'^question/(?P<question>[^/]+)/?','qa.views.test', name='qa_test' ),
]
