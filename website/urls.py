from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

website_views = [
    url(r'^$', views.index, name='index'),
    url(r'register/', views.new_registration, name='register'),
    url(r'login/', views.login, name='login'),
    url(r'main/', views.main, name='main'),
    url(r'articles/(?P<urlname>[a-z0-9_\-]+)/$', views.article, name='articles'),
    url(r'articles/(?P<urlname>[a-z0-9_\-]+)/edit/$', views.article_edit, name='article_edit'),
    url(r'comment/(?P<urlname>[a-z0-9_\-]+)/$', views.new_comment, name='new_comment'),
    url(r'new/', views.new_article, name='new_article'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'user/(?P<username>[a-zA-Z0-9]+)/$', views.profiles, name='profiles'),
    url(r'user/(?P<username>[a-zA-Z0-9]+)/following$', views.following, name='following'),
    url(r'search/', views.search, name='search'),
    url(r'guilds/$', views.guild_list, name='guild_list'),
    url(r'guilds/create/$', views.guild_create, name='guild_create'),
    url(r'guilds/(?P<guild_id>[a-f0-9]+)/$', views.guild_info, name='guild_info'),
    url(r'guilds/(?P<guild_id>[a-f0-9]+)/join/$', views.guild_join, name='guild_join'),
    url(r'guilds/(?P<guild_id>[a-f0-9]+)/leave/$', views.guild_leave, name='guild_leave'),
    url(r'guilds/(?P<guild_id>[a-f0-9]+)/edit/$', views.guild_edit, name='guild_edit'),
    url(r'guilds/(?P<guild_id>[a-f0-9]+)/edit/disband$', views.guild_disband, name='guild_disband'),
]

restframework = [
    url(r'api/', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls')),
    url(r'ratings/$', views.RatingsList.as_view()),
    url(r'ratings/(?P<urlname>[a-z0-9_\-]+)/$', views.RatingDetail.as_view()),
]

urlpatterns = website_views + restframework
