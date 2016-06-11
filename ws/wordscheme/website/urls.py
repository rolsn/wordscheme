from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login

from . import views

app_name="website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.new_registration, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^main/', views.main, name='main'),
    url(r'^articles/(?P<id>[0-9]+)/$', views.article, name='articles'),
    url(r'^logout/', logout_then_login),
]
