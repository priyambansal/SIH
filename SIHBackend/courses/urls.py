from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^undergraduate/$', views.undergraduate, name='undergraduate'),	
	url(r'^postgraduate/$', views.postgraduate, name='postgraduate'),
	url(r'^ugscience/$', views.ugscience, name= 'ugscience'),
	url(r'^technology/$', views.technology, name= 'technology'),
	url(r'^arts/$', views.arts, name= 'arts'),
	url(r'^architecture/$', views.architecture, name= 'architecture'),
	url(r'^management/$', views.management, name= 'management'),
    url(r'^commerce/$', views.commerce, name= 'commerce'),
 	   
]