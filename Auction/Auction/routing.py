from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import AppAuctionItem.routing


application = ProtocolTypeRouter({
 
 'websocket': AuthMiddlewareStack(
     
    URLRouter(
    AppAuctionItem.routing.websocket_urlpatterns
    )
 ),
})