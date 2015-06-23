from django.conf.urls import patterns, url
from base import views
from base.views import UserListView

urlpatterns = patterns('',
        url(r'^register/$', views.register, name='register'),
        url(r'^users/userupdate/(\d+)/$', views.userupdate, name='edit'),
        url(r'^users/userdelete/(\d+)/$', views.userdelete, name='delete'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^index/', views.index, name='index'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^phonetics/$', views.phonetics, name='phonetics'),
        url(r'^english/$', views.english, name='english'),
        url(r'^englishtest2/$', views.englishtest2, name='englishtest2'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^users/$', views.UserListView.as_view(), name='user-list'),
        url(r'^cardgame/$', views.cardgame, name='cardgame'),
        url(r'^$', views.index, name='index'),
	url(r'^submit/$', views.submit_click, name='submit'),
        )
