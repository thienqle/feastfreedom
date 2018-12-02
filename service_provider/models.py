from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Provider(models.Model):
    user_id = models.ForeignKey(User, null=True, related_name="provider", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Kitchen(models.Model):
    provider_id = models.ForeignKey(Provider, null=False, related_name="provider",on_delete = models.CASCADE)
    kit_days = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    kit_image = models.ImageField(upload_to="", blank=True, null=True)  #Leave blank to upload to current media folder under root
class Menu(models.Model):
    kit_id = models.ForeignKey(Kitchen, null=False, related_name="kitchen",on_delete = models.CASCADE)
    veg = models.BooleanField(default = False)
    price = models.IntegerField(default=0)
    item_name=models.CharField(max_length=200)
