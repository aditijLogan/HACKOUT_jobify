from django.db import models

# Create your models here.
class Employer(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    email = models.TextField()
    phone = models.BigIntegerField()
    WorkAddress=models.TextField()
    reqGender = models.TextField()
    reqQualification = models.TextField()
    reqVacancy = models.TextField()