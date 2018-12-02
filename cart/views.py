from django.shortcuts import render,redirect
from django.http import HttpResponse
from service_provider.models import Kitchen,Provider,Menu

# Create your views here.
def cart(request):
    #old_dishes = request.session.get('old_items')
    indexes = request.POST.getlist('items')
    total = 0
    if not 'old_dishes' in request.session or not request.session['old_dishes']:
        request.session['old_dishes'] = []
        dishes = []
        for index in indexes:
            dish = Menu.objects.get(id=index)
            dishes.append(dish)
            total += dish.price
            request.session['old_dishes'].append(int(index))
    else:
        dishes = []
        for index in request.session['old_dishes']:
            if index not in indexes:
                indexes.append(index)
        for index in indexes:
            if index not in request.session['old_dishes']:
                request.session['old_dishes'].append(int(index))
            dish = Menu.objects.get(id=index)
            dishes.append(dish)
            total += dish.price

    # return redirect('index')    # Using the name in routing
    quantity = 0
    if not 'old_dishes' in request.session or not request.session['old_dishes']:
        quanity = 0
    else:
        quantity = len(request.session['old_dishes'])
    kitchens = Kitchen.objects.all()

    return render(request,'cart/cart.html',{'dishes':dishes,'total':total,'quantity':quantity})

def delete_item(request,id):
    old_dishes = request.session.get('old_items')
    request.session.modified = True
    if not 'old_dishes' in request.session or not request.session['old_dishes']:
        return redirect('cart')
    else:
        #if id in request.session['old_dishes']:
        request.session['old_dishes'].remove(int(id))
    return redirect('cart')

def place_order(request):
    if request.user:
        if request.user.is_authenticated:
            del request.session['old_dishes']
            return render(request,'cart/checkout.html',{})
        else:
            return redirect('login')
    else:
        return redirect('login')
