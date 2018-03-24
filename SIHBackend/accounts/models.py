from django.db import models
from django.contrib.auth.models import User


class CommonRegistration(models.Model):
	user=models.ForeignKey(User,related_name='registrationInfo',on_delete=models.CASCADE)
	# for name and email
	Contact=models.IntegerField(max_length=20)
	DateOfBirth=models.DateField(max_length=8)
	Address=models.TextField(max_length=500)
	GENDER_CHOICES =(
		('M','Male'),
		('F','Female'),
		)
	Gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
	Passport_number=models.IntegerField(max_length=9)
	Religion=models.CharField(max_length=10)
	Nationality=models.CharField(max_length=20)
	# qualification=models.ForeignKey(max_length=10)
	School=models.CharField(max_length=100)
	University=models.CharField(max_length=100)
	Marks_highschool=models.IntegerField(max_length=2)
	Marks_inter=models.IntegerField(max_length=2,default='0')
	Marks_university=models.IntegerField(max_length=2)
    
    	
# Create your models here.
