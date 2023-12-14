from django.db import models

# Create your models here.

class users(models.Model):
    First_Name=models.CharField(max_length=15)
    Last_Name=models.CharField(max_length=15)
    age=models.IntegerField()
    
    place=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=15)
