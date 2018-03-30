from django.db import models


class Category(models.Model):
	Field=models.CharField(max_length=100)
	Degree=models.CharField(max_length=100)
	Address=models.CharField(max_length=500)
	College=models.CharField(max_length=100)
	Exam=models.CharField(max_length=100)
# Create your models here.
