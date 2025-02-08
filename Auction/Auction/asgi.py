# auction/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path  # Thêm dòng nhập khẩu này
from AppAuctionItem.consumers import ChatConsumer  # Import your consumer

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Auction.settings')

# Define the ASGI application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles HTTP requests
    "websocket": AuthMiddlewareStack(  # Handles WebSocket connections
        URLRouter([
            path('ws/auction/<int:item_id>/<str:item_name>/', ChatConsumer.as_asgi()),
        ])
    ),
})
