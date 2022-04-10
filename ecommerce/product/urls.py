from django import urls
from django.urls import path

from .views import *

app_name = 'product'
urlpatterns = [
    path('<pk>', ProdectDetailView.as_view(), name='product_details'),
]


