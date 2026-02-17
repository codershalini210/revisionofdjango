from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Cuisine
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    return HttpResponse("welcome to home of first app ")

def Cuisine_list(request):
    objlist = Cuisine.objects.all()
    paginator = Paginator(objlist,2)  # 2 items in each page
    page = request.GET.get('page')

    try:
        cuisines = paginator.page(page)
     
    except PageNotAnInteger:
        cuisines= paginator.page(1)
    except EmptyPage:
        cuisines = paginator.page(paginator.num_pages)

    return render(request,"firstapp/cuisine_list.html",{'page':page,'cuisines':cuisines})
def Cuisine_detail(request,pk):
    cuisine_selected = get_object_or_404(Cuisine,pk=pk,status='published')
    
    context = {'cuisine': cuisine_selected}
    
    return render(request,'firstapp/cuisine_details.html',context)