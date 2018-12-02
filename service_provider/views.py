from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Kitchen,Provider,Menu
from .forms import ProviderForm,KitchenForm,MenuForm
from regular_user.models import UserType


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import formset_factory

# Create your views here.
def kitchen_detail(request, id):
    provider = Provider.objects.get(id=id)
    kitchen = Kitchen.objects.get(provider_id = provider)
    dishes = Menu.objects.filter(kit_id = kitchen)

    quantity = 0
    if not 'old_dishes' in request.session or not request.session['old_dishes']:
        quanity = 0
    else:
        quantity = len(request.session['old_dishes'])

    return render(request,'service_provider/kitchen_detail.html',{'kitchen':kitchen,'dishes':dishes,'quantity':quantity})
    #return HttpResponse(dishes)


def log_out(request):
    logout(request)
    return redirect('index')    # Using the name in


def signup(request):
    form = ProviderForm(request.POST)
    if form.is_valid():
        if User.objects.filter(username=form.cleaned_data['username']).exists():
            message = "User name is already exist."
            return render(request, 'service_provider/signup_form.html', {'form': ProviderForm(), "message": message})
        user = User()
        user.username = form.cleaned_data.get('username')
        user.email = form.cleaned_data['email'];
        user.set_password(form.cleaned_data.get('password'))
        user.save()
        new_provider = Provider()
        new_provider.user_id = user
        new_provider.name = user.username
        new_provider.save()
        user_type = UserType()
        user_type.user_id = user
        user_type.role = 'provider'
        user_type.save()
        login(request, user)  # login after signup
    else:
        new_form = ProviderForm()
        return render(request, 'service_provider/signup_form.html', {'form': new_form})  # variable always name form

    return redirect('signup_kitchen',id=0)

def submit_kitchen(request):
    form = KitchenForm(request.POST,request.FILES)
    menusFormset = formset_factory(MenuForm)
    menus = menusFormset(request.POST,request.FILES)

    if form.is_valid() and menus.is_valid():
        provider = Provider.objects.get(user_id = request.user)
        kitchen = Kitchen()
        kitchen.provider_id = provider
        request.session['mon'] = form.cleaned_data['mon']
        request.session['tue'] = form.cleaned_data['tue']
        request.session['wed'] = form.cleaned_data['wed']
        request.session['thu'] = form.cleaned_data['thu']
        request.session['fri'] = form.cleaned_data['fri']
        request.session['sat'] = form.cleaned_data['sat']
        request.session['sun'] = form.cleaned_data['sun']
        request.session['start_time'] = form.cleaned_data['start_time']
        request.session['end_time'] = form.cleaned_data['end_time']
        #request.session['image'] = form.cleaned_data['image']
        workdays = ''
        if form.cleaned_data['mon'] == True:
            workdays += 'M,'
        if form.cleaned_data['tue'] == True:
            workdays += 'T,'
        if form.cleaned_data['wed'] == True:
            workdays += 'W,'
        if form.cleaned_data['thu'] == True:
            workdays += 'T,'
        if form.cleaned_data['fri'] == True:
            workdays += 'F,'
        if form.cleaned_data['sat'] == True:
            workdays += 'S,'
        if form.cleaned_data['sun'] == True:
            workdays += 'S,'
        workdays = workdays[0:len(workdays)-1]
        kitchen.kit_days = workdays
        kitchen.start_time = form.cleaned_data['start_time']
        kitchen.end_time = form.cleaned_data['end_time']
        kitchen.kit_image = form.cleaned_data['image']
        kitchen.save()

        for menu in menus:
            dish = Menu()
            dish.kit_id = kitchen
            dish.item_name = menu.cleaned_data['item_name']
            dish.veg = menu.cleaned_data['veg']
            dish.price = menu.cleaned_data['price']
            dish.save()

    else:
        menusFormset = formset_factory(MenuForm)
        menus = menusFormset(request.POST)
        #return render(request, 'service_provider/signup_kitchen_form.html', {'form': new_form,'menus':menus,'role':type})  # variable always name form
        return redirect('signup_kitchen', id=len(menus))

    return render(request, 'index.html', {})

def signup_kitchen_n(request,id):
    form = KitchenForm(request.POST,request.FILES)
    new_form = KitchenForm()
    if form.is_valid():
        provider = Provider.objects.get(user_id=request.user)
        kitchen = Kitchen()
        kitchen.provider_id = provider
        request.session['mon'] = form.cleaned_data['mon']
        request.session['tue'] = form.cleaned_data['tue']
        request.session['wed'] = form.cleaned_data['wed']
        request.session['thu'] = form.cleaned_data['thu']
        request.session['fri'] = form.cleaned_data['fri']
        request.session['sat'] = form.cleaned_data['sat']
        request.session['sun'] = form.cleaned_data['sun']
        request.session['start_time'] = form.cleaned_data['start_time']
        request.session['end_time'] = form.cleaned_data['end_time']
        #request.session['image'] = form.cleaned_data['image']
        workdays = ''
        if form.cleaned_data['mon'] == True:
            workdays += 'M,'
        if form.cleaned_data['tue'] == True:
            workdays += 'T,'
        if form.cleaned_data['wed'] == True:
            workdays += 'W,'
        if form.cleaned_data['thu'] == True:
            workdays += 'T,'
        if form.cleaned_data['fri'] == True:
            workdays += 'F,'
        if form.cleaned_data['sat'] == True:
            workdays += 'S,'
        if form.cleaned_data['sun'] == True:
            workdays += 'S,'
        workdays = workdays[0:len(workdays) - 1]
        kitchen.kit_days = workdays
        kitchen.start_time = form.cleaned_data['start_time']
        kitchen.end_time = form.cleaned_data['end_time']
        kitchen.kit_image = form.cleaned_data['image']

    menusFormset = formset_factory(MenuForm,extra=int(id)+1)
    menus = menusFormset()
    type = 'customer'
    if request.user.is_authenticated:
        try:
            userType = UserType.objects.get(user_id=request.user)
            type = userType.role
        except:
            type = 'customer'

    return render(request, 'service_provider/signup_kitchen_form.html', {'form': new_form,'menus':menus,'role':type})  # variable always name form
