from django.conf.urls import patterns, include, url
from django.contrib import admin

import match_service.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VideoRetrivial2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^m/', include(match_service.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
