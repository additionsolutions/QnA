from django.conf.urls import patterns, include, url
from django.contrib import admin
from base import views
from django.conf import settings
    
urlpatterns = patterns('',
    # Examples:
    #url (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^addsol/', include(admin.site.urls)),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^excelencia/', views.excelencia, name='excelencia'),
    url(r'^qna/', views.qna, name='qna'),
    url(r'^c/', include('contents.urls')),
    url(r'^p/', include('ptest.urls')),
    url(r'^t/', include('etests.urls')),
    url(r'^m/', include('messaging.urls')),
    #url(r'^dmin/', include('dmin.urls')),
    url(r'^a/', include('dmin.urls')),
    url(r'^base/', include('base.urls')),
    url(r'^$', include('base.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)
