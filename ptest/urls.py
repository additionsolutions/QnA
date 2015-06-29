from django.conf.urls import patterns, url
from ptest import views
from etests import views as vw

urlpatterns = patterns('',
        url(r'^ptest/$', views.exam, name='exam'),
        url(r'^ptest/examlist$', views.examlist, name='examlist'),
        url(r'^ptest/grade/$', views.grade, name='grade'),
        url(r'^ptest/(\d{1,2})/$', views.exam, name='exam'),
        url(r'^ptest/sr/(\d{1,2})/$', views.examsr, name='examsr'),
        url(r'^ptest/gradeit/(\d{1,2})/(\d{1,2})$',views.gradeit, name='gradeit'),
        )
