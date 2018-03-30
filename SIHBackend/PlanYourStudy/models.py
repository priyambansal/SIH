from django.db import models


class Category(models.Model):
	Field=models.CharField(max_length=100)
	Degree=models.CharField(max_length=100)
	Address=models.CharField(max_length=500)
	College=models.CharField(max_length=100)
	Exam=models.CharField(max_length=100)
	Fees=models.IntegerField(default="0")
	CHOICES=(
		('Government','Government'),
		('Private','Private'),)
	InstituteType=models.CharField(max_length=100,choices=CHOICES,default="Government")
	Check = models.BooleanField(default=False)
    
# Create your models here.
