from django.shortcuts import render,redirect
from django.http import HttpResponse
from service_provider.models import Kitchen,Provider,Menu

# Create your views here.
def cart(request):
    dishes_id = request.POST.getlist('items')
    request.session.modified = True
    total = 0
    quantity = 0
    dishes = []
    if not 'dishes' in request.session or not request.session['dishes']:
        request.session['dishes'] = []
        for dish_id in dishes_id:
            request.session['dishes'].append(dish_id)
            quantity += 1
            dish = Menu.objects.get(id=dish_id)
            dishes.append(dish)
            total += dish.price
    else:
        for dish_id in dishes_id:
            request.session['dishes'].append(dish_id)
        for dish_id in request.session['dishes']:
            quantity += 1
            dish = Menu.objects.get(id=dish_id)
            total += dish.price
            dishes.append(dish)

    return render(request,'cart/cart.html',{'dishes':dishes,'total':total,'quantity':quantity})

def delete_item(request,id):
    request.session.modified = True
    if not 'dishes' in request.session or not request.session['dishes']:
        return redirect('cart')
    else:
        request.session['dishes'].remove(id)
    return redirect('cart')

def place_order(request):
    if request.user:
        if request.user.is_authenticated:
            del request.session['dishes']
            return render(request,'cart/checkout.html',{})

    return redirect('login')
