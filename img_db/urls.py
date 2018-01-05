# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Fiv'
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload', views.uploadImg),
    url(r'^show', views.showImg),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)