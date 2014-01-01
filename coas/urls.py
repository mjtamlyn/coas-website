from django.conf.urls import include
from django.contrib import admin

from cbvpatterns import patterns, url


urlpatterns = patterns('coas.views',
    url(r'^$', 'Home', name='home'),
    url(r'^clubs/$', 'Clubs', name='clubs'),

    url(r'^admin/', include(admin.site.urls)),
)
