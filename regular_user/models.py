from django.db import models

# Create your models here.
class RegularUser(models.Model):
    fname = models.TextField(blank=True, null=True)
    lname = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    ques1 = models.TextField(blank=True, null=True)
    ans1 = models.TextField(blank=True, null=True)
    ques2 = models.TextField(blank=True, null=True)
    ans2 = models.TextField(blank=True, null=True)
