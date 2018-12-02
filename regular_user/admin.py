from django.contrib import admin
from .models import RegularUser,UserType

# Register your models here.
admin.site.register(RegularUser)
admin.site.register(UserType)