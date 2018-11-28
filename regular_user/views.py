from django.shortcuts import render
from service_provider.models import Kitchen,Menu,Provider

# Create your views here.
def list_all_kitchen(request):
    kitchens = Kitchen.objects.all()
    #providers = Kitchen.provider.all()
    #return render(request,'index.html',{'kitchens':kitchens,'providers':providers})
    return render(request,'index.html',{'kitchens':kitchens})

#def login(request)
#   return render(request,'index.html',{})