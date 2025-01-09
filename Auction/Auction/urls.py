from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('AppAuction.urls'),name='auction-page'),
    path('auction/',include('AppAuctionItem.urls',namespace='auction'),name="auctionitem-page"),
    path('accounts/',include('Accounts.urls'),name='accounts-page'),
    path('blog/',include('Blog.urls'),name='blog-app'),
    

    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)