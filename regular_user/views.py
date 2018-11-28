from django.shortcuts import render
from service_provider.models import Kitchen,Menu

# Create your views here.
def list_all_kitchen(request):
    kitchens = Kitchen.objects.all()
    return render(request,'index.html',{'kitchens':kitchens})

#def login(request)
#   return render(request,'index.html',{})