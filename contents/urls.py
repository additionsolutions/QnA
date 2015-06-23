from django.conf.urls import patterns, url
from contents import views

urlpatterns = patterns('',
        #url(r'^academicduration/$', views.academicduration, name='academicduration'),
        #url(r'^add_contenttype/$', views.add_contenttype, name='add_contenttype'),
        #url(r'^type/$', views.contentstype, name='contentstype'),
        #url(r'^contents/$', views.contents, name='contents'),
        #url(r'^permissions/$', views.permissions, name='permissions'),
        url(r'^contenttype/$', views.contenttype_list, name='contenttype_list'),
        url(r'^contenttype/new$', views.contenttype_create, name='contenttype_new'),
        url(r'^contenttype/edit/(?P<pk>\d+)$', views.contenttype_update, name='contenttype_edit'),
        url(r'^contenttype/delete/(?P<pk>\d+)$',views.contenttype_delete, name='contenttype_delete'),
        #url(r'^content/$', views.ContentCreateView, name='content_list'),
        url(r'^content/$', views.content_list, name='content_list'),
        url(r'^content_data/(\d{1,2})/$', views.content_data, name='content_data'),
        url(r'^content/new$', views.content_create, name='content_new'),
        url(r'^content/edit/(?P<pk>\d+)$', views.content_update, name='content_edit'),
        url(r'^content/delete/(?P<pk>\d+)$',views.content_delete, name='content_delete'),
        url(r'^content/notice$', views.content, name='Notice'),
        url(r'^content/activities$', views.content, name='Activities'),
        url(r'^content/portion$', views.content, name='Portion'),
        )