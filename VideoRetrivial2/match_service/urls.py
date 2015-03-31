#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Ruslan Talipov'

from django.conf.urls import patterns, include, url

from match_service.views import match_page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VideoRetrivial2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^video/$', match_page),
)
