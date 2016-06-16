from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login

from . import views

app_name="website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/', views.new_registration, name='register'),
    url(r'login/', views.login, name='login'),
    url(r'main/', views.main, name='main'),
    url(r'articles/(?P<id>[0-9]+)/$', views.article, name='articles'),
    url(r'comment/(?P<article_id>[0-9]+)/$', views.new_comment, name='new_comment'),
    url(r'new/', views.new_article, name='new_article'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'users/(?P<username>[a-zA-Z0-9]+)/$', views.user, name='users'),
    url(r'search/(?P<search_term>[a-zA-Z0-9]+)/$', views.search, name='search'),
]
