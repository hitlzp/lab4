from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from book.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^view_all/$',view_all),
    url(r'^add/$',addbooks),
    url(r'^search/$',search),
    url(r'^delete/$',delete),
    url(r'^change/$',change),
    url(r'^list/$',list),
    url(r'^show/$',show),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT }),
    # Examples:
    url(r'^$', 'bookdemo.views.home', name='home'),
    url(r'^bookdemo/', include('bookdemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
