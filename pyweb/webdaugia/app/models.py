from django.db import models
from django.contrib.auth.models import User

# Customer để lưu thông tin người dùng
class Customer(models.Model):  
    user = model.OneToOneFielld(User,on_delete=model.SET_BULL,null=True,blank=False)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name or self.username  # Trả về tên hoặc username nếu tên null

# Product để lưu thông tin trang sức
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)  # Tên sản phẩm
    price = models.FloatField()  # Giá sản phẩm
    digital = models.BooleanField(default=False, null=True, blank=True)  # Sản phẩm vật lý hay không

    def __str__(self):
        return self.name  # Trả về tên sản phẩm

# Auction để lưu thông tin phiên đấu giá
class Auction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)  # Liên kết với khách hàng
    start_time = models.DateTimeField()  # Thời gian bắt đầu
    end_time = models.DateTimeField()  # Thời gian kết thúc
    name = models.CharField(max_length=200, null=True)  # Tên phiên đấu giá
    transaction_id = models.CharField(max_length=200, null=True, blank=True)  # Mã giao dịch (không bắt buộc)
    status = models.CharField(max_length=50, default="Pending")  # Trạng thái (Pending, Ongoing, Completed)
    winner = models.ForeignKey(Customer, related_name='won_auctions', on_delete=models.SET_NULL, null=True, blank=True)  # Người thắng đấu giá
    notification_sent = models.BooleanField(default=False)  # Trạng thái gửi thông báo

    def __str__(self):
        return self.name or str(self.id)  # Tên phiên đấu giá hoặc ID nếu tên null

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
    address = models.CharField(max_length=200, null=True)  # Địa chỉ
    city = models.CharField(max_length=200, null=True)  # Thành phố
    mobile = models.CharField(max_length=10, null=True)  # Điện thoại liên hệ
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
    payment_method = models.CharField(max_length=50, null=True)  # Phương thức thanh toán
    payment_status = models.CharField(max_length=50, default="Pending")  # Trạng thái thanh toán
    total_amount = models.FloatField()  # Tổng tiền

    def __str__(self):
        return f"Payment for {self.auction.name if self.auction else 'Unknown Auction'} - {self.payment_status}"
