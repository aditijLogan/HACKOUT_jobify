from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.TextField()
    age = models.TextField()
    phone = models.BigIntegerField()
    email = models.TextField()
    skills = models.TextField()
    education = models.TextField()
    address = models.TextField()
    aadhar = models.BigIntegerField()
    gender = models.TextField()


