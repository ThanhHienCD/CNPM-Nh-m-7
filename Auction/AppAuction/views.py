from django.shortcuts import render
from django.http import HttpResponse
from AppAuctionItem.models import Lot
from math import ceil
from AppAuctionItem.models import Category

# Create your views here.

def index(request):
    
    categories = Category.objects.all()
    context ={
        'items_live' : Lot.objects.filter(is_live=True)[:4],
        'items_trending': Lot.objects.filter(is_trending=True)[:8],
        'items_banner' : Lot.objects.filter(on_banner=True),
        'items':Lot.objects.all()[:4],
        'category':categories,
      
    }
    
    
    return render(request,'AppAuction/index.html',context)
 
def about(request):
    return render(request,'AppAuction/about.html')

def contact_us(request):
    return render(request,'AppAuction/contact_us.html')