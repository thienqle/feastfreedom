from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Kitchen,Provider,Menu

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

    return render(request,'service_provider/kitchen_detail.html',{'dishes':dishes,'quantity':quantity})
    #return HttpResponse(dishes)
