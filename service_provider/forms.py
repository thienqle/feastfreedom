from django.forms import ModelForm
from .models import Provider,Kitchen,Menu
from django import forms


class ProviderForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput,label="Confirm Password")

HOURS_LISTS = [
    ('00:00 AM','00:00 AM'),
    ('01:00 AM','01:00 AM'),
    ('02:00 AM','02:00 AM'),
    ('03:00 AM','03:00 AM'),
    ('04:00 AM','04:00 AM'),
    ('05:00 AM','05:00 AM'),
    ('06:00 AM','06:00 AM'),
    ('07:00 AM','07:00 AM'),
    ('08:00 AM','08:00 AM'),
    ('09:00 AM','09:00 AM'),
    ('10:00 AM','10:00 AM'),
    ('11:00 AM','11:00 AM'),
    ('12:00 AM','12:00 AM'),
    ('01:00 PM','01:00 PM'),
    ('02:00 PM','02:00 PM'),
    ('03:00 PM','03:00 PM'),
    ('04:00 PM','04:00 PM'),
    ('05:00 PM','05:00 PM'),
    ('06:00 PM','06:00 PM'),
    ('07:00 PM','07:00 PM'),
    ('08:00 PM','08:00 PM'),
    ('09:00 PM','09:00 PM'),
    ('10:00 PM','10:00 PM'),
    ('11:00 PM','11:00 PM'),
]

class KitchenForm(forms.Form):
    mon = forms.BooleanField(initial=True,required=False)
    tue = forms.BooleanField(initial=True,required=False)
    wed = forms.BooleanField(initial=True,required=False)
    thu = forms.BooleanField(initial=True,required=False)
    fri = forms.BooleanField(initial=True,required=False)
    sat = forms.BooleanField(initial=True,required=False)
    sun = forms.BooleanField(initial=True,required=False)
    start_time = forms.CharField(label='Start time',widget=forms.Select(choices=HOURS_LISTS))
    end_time = forms.CharField(label='End time',widget=forms.Select(choices=HOURS_LISTS))
    image = forms.ImageField(required=False)

class MenuForm(forms.Form):
    item_name = forms.CharField(max_length=100)
    veg = forms.BooleanField(required=False)
    price = forms.DecimalField()


