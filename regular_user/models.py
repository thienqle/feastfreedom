from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegularUser(models.Model):
    user_id = models.ForeignKey(User, null=True, related_name="user",on_delete = models.CASCADE)
    ques1 = models.TextField(blank=True, null=True)
    ans1 = models.TextField(blank=True, null=True)
    ques2 = models.TextField(blank=True, null=True)
    ans2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_id.username

class UserType(models.Model):
    user_id = models.ForeignKey(User, null=True, related_name="regular_user", on_delete=models.CASCADE)     # cannot use same related_name
    role = models.TextField(blank=True, null=True)
