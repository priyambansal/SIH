from django.db import models
from django.contrib.auth.models import User


class CommonRegistration(models.Model):
	User_name=models.CharField(max_length=30,default="")
	User_email=models.EmailField(max_length=30,default="")
	# for name and email
	Contact=models.IntegerField()
	DateOfBirth=models.DateField(max_length=8)
	Address=models.TextField(max_length=500)
	GENDER_CHOICES =(
		('M','Male'),
		('F','Female'),
		)
	Gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
	Passport_number=models.IntegerField()
	Religion=models.CharField(max_length=10)
	Nationality=models.CharField(max_length=20)
	# qualification=models.ForeignKey(max_length=10)
	School=models.CharField(max_length=100)
	University=models.CharField(max_length=100)
	Marks_highschool=models.IntegerField()
	Marks_inter=models.IntegerField()
	Marks_university=models.IntegerField()
    
    	
# Create your models here.
