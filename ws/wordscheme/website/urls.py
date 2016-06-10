from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.new_registration, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^main/', views.main, name='main'),
]
