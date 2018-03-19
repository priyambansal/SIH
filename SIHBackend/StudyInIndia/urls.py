from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^WhyStudyInIndia/$', views.WhyStudyInIndia, name='WhyStudyInIndia'),	
	url(r'^StudyPermits/$', views.StudyPermits, name='StudyPermits'),
	url(r'^WorkOpp/$', views.WorkOpp, name='WorkOpp')
]