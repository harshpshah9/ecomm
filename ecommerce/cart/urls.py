from django.urls import path
from cart.views import AddToCart,CartListView,CartDeleteView,CartQtyChangeView,CheckoutCart
app_name='cart'
urlpatterns = [
   path('<int:productid>',AddToCart.as_view(),name='addcart'),
   path('list',CartListView.as_view(),name='list'),
   path('deletecart/<int:cart_item_id>',CartDeleteView.as_view(),name='delete_cart'),
   path('updatecart',CartQtyChangeView.as_view(),name='update_cart'),
   path('checkout',CheckoutCart.as_view(),name='checkout'),
]