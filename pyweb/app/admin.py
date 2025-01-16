from django.contrib import admin
from .models import Customer, Product, Auction, AuctionItem, ShippingAddress, BidHistory, Payment

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(AuctionItem)
admin.site.register(ShippingAddress)
admin.site.register(BidHistory)
admin.site.register(Payment)
