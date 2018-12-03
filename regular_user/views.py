from django.shortcuts import render,redirect
from service_provider.models import Kitchen,Menu,Provider
from .forms import UserForm,UserLoginForm
from .models import RegularUser,UserType
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def list_all_kitchen(request):
    quantity = 0
    if not 'dishes' in request.session or not request.session['dishes']:
        quanity = 0
    else:
        quantity = len(request.session['dishes'])
    kitchens = Kitchen.objects.all()
    type = 'customer'
    if request.user.is_authenticated:
        try:
            userType = UserType.objects.get(user_id = request.user)
            type = userType.role
        except:
            type = 'customer'
    return render(request,'index.html',{'kitchens':kitchens,'quantity':quantity,'userType':type})

def signup(request):
    form = UserForm(request.POST)
    if form.is_valid():
        if User.objects.filter(username=form.cleaned_data['username']).exists():
            message = "User name is already exist."
            return render(request, 'regular_user/signup_form.html', {'form': UserForm(),"message":message})
        user = User()
        user.username = form.cleaned_data.get('username')
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
        user_type = UserType()
        user_type.user_id = user
        user_type.role = 'customer'
        user_type.save()
        login(request,user)     #login after signup
    else:
        new_user_form = UserForm()
        return render(request,'regular_user/signup_form.html',{'form':new_user_form})   # variable always name form

    return render(request,'index.html',{})


def log_out(request):
    logout(request)
    return redirect('index')    # Using the name in 