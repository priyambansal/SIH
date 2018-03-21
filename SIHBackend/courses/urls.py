from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^undergraduate/$', views.undergraduate, name='undergraduate'),	
	url(r'^postgraduate/$', views.postgraduate, name='postgraduate'),

]