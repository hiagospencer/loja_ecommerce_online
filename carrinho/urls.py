from django.urls import path
from .views import cart_home, cart_update


app_name = 'cart'

urlpatterns = [
    path('carrinho/', cart_home, name='carrinho'),
    path('update/', cart_update, name='update')

]