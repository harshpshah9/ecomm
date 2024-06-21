from django.urls import path
from .views import AdminOrderDetailView, AdminOrderListView, OrderStatusUpdateView, PlaceorderView,OrderListView,OrderDetailView
app_name='order'
urlpatterns = [
    path('placeorder/', PlaceorderView.as_view(),name='placeorder'),
    path('list/',OrderListView.as_view(),name='order_lists'),
    path('view/<int:pk>',OrderDetailView.as_view(),name='order_details'),
    path('orderlist/',AdminOrderListView.as_view(),name='order_admin_list'),
    path('orderdetails/<int:pk>',AdminOrderDetailView.as_view(),name='order_admin_details'),
    path('status/update/<int:pk>',OrderStatusUpdateView.as_view(),name='order_status_update'),
  ]