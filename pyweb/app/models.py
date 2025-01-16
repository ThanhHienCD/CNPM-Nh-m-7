from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Customer để lưu thông tin người dùng
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name or self.user.username  # Trả về tên hoặc username nếu tên null
    
#Product

# Auction để lưu thông tin phiên đấu giá
class Auction(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Đang diễn ra'),
        ('upcoming', 'Sắp diễn ra'),
        ('ended', 'Kết thúc'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)  # Cho phép trường end_time null
    name = models.CharField(max_length=200, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)
    winner = models.ForeignKey(Customer, related_name='won_auctions', on_delete=models.SET_NULL, null=True, blank=True)
    notification_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.name or f"Auction {self.id}"

#Product
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    time = models.DateTimeField(null=True, blank=True)  # Cho phép trường time nhận giá trị null
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, blank=True, null=True)  # Liên kết với Auction
    image = models.ImageField (null=True,blank=True)
     
    def __str__(self):
        return self.name  # Trả về tên sản phẩm

    @property
    def ImageURL(self):
        try:
            url=self.image.url
        except:
            url = ''
        return url

# AuctionItem để lưu thông tin trang sức trong mỗi phiên đấu giá
class AuctionItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)  # Sản phẩm
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, blank=True, null=True)  # Phiên đấu giá
    quantity = models.IntegerField(default=0, null=True, blank=True)  # Số lượng sản phẩm

    def __str__(self):
        return f"{self.product.name} in {self.auction.name}" if self.product and self.auction else "Unknown Item"

# ShippingAddress để lưu thông tin địa chỉ giao hàng
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)  # Khách hàng
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, blank=True, null=True)  # Phiên đấu giá
    address = models.CharField(max_length=200, null=True, blank=True)  # Địa chỉ
    city = models.CharField(max_length=200, null=True, blank=True)  # Thành phố
    mobile = models.CharField(max_length=10, null=True, blank=True)  # Điện thoại liên hệ
    date_added = models.DateTimeField(auto_now_add=True)  # Ngày thêm
    other_info = models.CharField(max_length=200, null=True, blank=True)  # Thông tin bổ sung

    def __str__(self):
        return self.address or "No Address"

# BidHistory lưu lịch sử các cuộc đấu giá
class BidHistory(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)  # Phiên đấu giá
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Khách hàng
    bid_amount = models.FloatField()  # Mức giá đặt
    bid_time = models.DateTimeField(auto_now_add=True)  # Thời gian đặt giá

    def __str__(self):
        return f"{self.customer.name} bid {self.bid_amount} on {self.auction.name}"

# Payment để lưu thông tin thanh toán
class Payment(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, blank=True, null=True)  # Phiên đấu giá
    payment_method = models.CharField(max_length=50, null=True, blank=True)  # Phương thức thanh toán
    payment_status = models.CharField(max_length=50, default="Pending")  # Trạng thái thanh toán
    total_amount = models.FloatField()  # Tổng tiền

    def __str__(self):
        return f"Payment for {self.auction.name if self.auction else 'Unknown Auction'} - {self.payment_status}"
