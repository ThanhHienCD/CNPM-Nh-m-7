from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Auction  # Import các model

# Create your views here.
def home(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm
    auctions = Auction.objects.all()  # Lấy tất cả các phiên đấu giá
    context = {'products': products, 'auctions': auctions}
    return render(request, 'app/home.html', context)

def pas(request):
    context = {}
    return render(request, 'app/pas.html', context)

def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)
