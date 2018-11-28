from django.db import models

# Create your models here.
class RegularUser(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    question1 = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=200)
    question2 = models.CharField(max_length=200)
    answer2 = models.CharField(max_length=200)