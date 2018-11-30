from django.shortcuts import render,redirect
from service_provider.models import Kitchen,Menu,Provider
from .forms import UserForm,UserLoginForm
from .models import RegularUser
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your views here.
def list_all_kitchen(request):
    quantity = 0
    if not 'old_dishes' in request.session or not request.session['old_dishes']:
        quanity = 0
    else:
        quantity = len(request.session['old_dishes'])
    kitchens = Kitchen.objects.all()
    return render(request,'index.html',{'kitchens':kitchens,'quantity':quantity})

def signup(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = User()
        user.username = form.cleaned_data.get('email')
        user.first_name = form.cleaned_data['firstName'];
        user.last_name = form.cleaned_data['lastName'];
        user.email = form.cleaned_data['email'];
        user.set_password(form.cleaned_data.get('password'))
        user.save()
        new_user = RegularUser()
        new_user.user_id = user
        new_user.ques1 = form.cleaned_data['secret_quesion1']
        new_user.ans1 = form.cleaned_data['answer1']
        new_user.ques2 = form.cleaned_data['secret_quesion2']
        new_user.ans2 = form.cleaned_data['answer1']
        new_user.save()
    else:
        new_user_form = UserForm()
        return render(request,'regular_user/signup_form.html',{'form':new_user_form})   # variable always name form

    return render(request,'index.html',{})


def log_out(request):
    logout(request)
    return redirect('index')    # Using the name in 