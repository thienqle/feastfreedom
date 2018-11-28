from django.shortcuts import render

# Create your views here.
def list_all_kitchen(request):
    return render(request,'index.html',{})
