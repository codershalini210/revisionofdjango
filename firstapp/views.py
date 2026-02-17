from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from .models import Cuisine
# Create your views here.
def home(request):
    return HttpResponse("welcome to home of first app ")

def Cuisine_list(request):
    cuisines = Cuisine.objects.all()
    context = {'cuisines':cuisines}
    return render(request,"firstapp/cuisine_list.html",context)
def Cuisine_detail(request,pk):
    cuisine_selected = get_list_or_404(Cuisine,pk=pk,status='published')
    context = {'cuisine': cuisine_selected}
    print(cuisine_selected)
    return render(request,'firstapp/cuisine_details.html',context)