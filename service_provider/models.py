from django.db import models

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
class Kitchen(models.Model):
    provider_id = models.ForeignKey(Provider, null=False, related_name="provider",on_delete = models.CASCADE)
    kit_days = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    kit_image = models.ImageField(upload_to="service_provider", blank=True, null=True)
class Menu(models.Model):
    kit_id = models.ForeignKey(Provider, null=False, related_name="kitchen",on_delete = models.CASCADE)
    item_name=models.CharField(max_length=200)