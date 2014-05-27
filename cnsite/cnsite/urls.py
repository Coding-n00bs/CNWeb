from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cnsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cnapp/', include('cnapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
