from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^login/$', login, {'template_name':'accounts/login.html'}),
	url(r'^logout/$', login, {'template_name':'accounts/logout.html'}),
	url(r'^signup/$', views.signup, name='signup'),	
	url(r'^register/$',views.register,name='register'),
	url(r'^exam/jee/$',views.jee,name='jee'),
	url(r'^exam/gate/$',views.gate,name='gate'),

]