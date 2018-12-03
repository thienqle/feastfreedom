from django.shortcuts import render,redirect
from django.http import HttpResponse
from service_provider.models import Kitchen,Provider,Menu
from django.core.mail import send_mail

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
            email_user = [request.user.email]
            email_prodvider = []

            for index in request.session['dishes']:
                dish = Menu.objects.get(id=index)
                email_prodvider.append(dish.kit_id.provider_id.user_id.email)

            del request.session['dishes']

            print(email_prodvider)
            send_mail('Order Confirmation form Feastfreedom',
                      'Thanks for making an order.',
                      'project510.summit@gmail.com',
                      email_user,
                      fail_silently=False,)
            send_mail('Order Confirmation form Feastfreedom',
                      'Your have a order from {}.'.format(email_user[0]),
                      'project510.summit@gmail.com',
                      email_prodvider,
                      fail_silently = False,)

        return render(request,'cart/checkout.html',{})

    return redirect('login')
