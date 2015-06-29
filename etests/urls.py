from django.conf.urls import patterns, url
from etests import views

urlpatterns = patterns('',
        url(r'^testset/$', views.testset, name='testset'),
        url(r'^testset/new$', views.testset_create, name='testset_new'),
        url(r'^testset/edit/(?P<pk>\d+)$', views.testset_update, name='testset_edit'),
        url(r'^testset/delete/(?P<pk>\d+)$', views.testset_delete, name='testset_delete'),
        url(r'^testsetline/edit/(?P<pk>\d+)$', views.testsetline_update, name='testsetline_edit'),
        url(r'^testsetline/delete/(?P<pk>\d+)$', views.testsetline_delete, name='testsetline_delete'),
        url(r'^testq/$', views.testq, name='testq'),
        url(r'^etest/$', views.etest, name='etest'),
        url(r'^etest/(\d{1,2})/$', views.etest, name='etest'),
        url(r'^etest/testlist$', views.testlist, name='testlist'),
        url(r'^etest/sr/(\d{1,2})/$', views.etestsr, name='etestsr'),
        url(r'^etest/ans/(\d{1,2})/$', views.etestans, name='etestans'),
        url(r'^etest/add/$', views.add_testset, name='add_testset'),
        url(r'^etest/q/(\d{1,2})/$', views.qetest, name='qetest'),
        )
