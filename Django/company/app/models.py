from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id=models.IntegerField()
    employee_name=models.CharField(max_length=20)
    Designation=models.CharField(max_length=15)
    Salary=models.IntegerField()
    Placr=models.CharField(max_length=25)

class Employ(models.Model):
    name=models.CharField(max_length=25)
    rollno=models.IntegerField()
    place=models.CharField(max_length=25)