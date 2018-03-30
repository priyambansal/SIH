from django.db import models


class Category(models.Model):
	Field=models.CharField(max_length=100)
	# Location_Choices=(
	# 	("North India","North india"),
	# 	("South India","South india"),
	# 	("East India","East india"),
	# 	("West India","West india"),)
	Degree=models.CharField(max_length=100)
	
	Location=models.CharField(max_length=500)
	College=models.CharField(max_length=100)
	Exam=models.CharField(max_length=100)
# Create your models here.
