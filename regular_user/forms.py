from django.forms import ModelForm
from .models import RegularUser
from django import forms


#List that is used in the dropdown list
QUESTION_LISTS = [
    ('Where is your hometown?','Where is your hometown?'),
    ('What is your first pet name?','What is your first pet name?')
]

class UserForm(forms.Form):
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    secret_quesion1 = forms.CharField(label='What is your first secret question?',widget=forms.Select(choices=QUESTION_LISTS))
    answer1 = forms.CharField(max_length=100)
    secret_quesion2 = forms.CharField(label='What is your second secret question?',widget=forms.Select(choices=QUESTION_LISTS))
    answer2 = forms.CharField(max_length=100)


class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
