from django.db import models
from base.base import BaseModel
from user.models import User, UserAddress
from product.models import Product
from django_extensions.db.models import *

choice = [('pending', 'pending'),
          ('onroad', 'onroad'),
          ('delivered', 'delivered')]

# Create your models here.
class Order(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddress, related_name='user_address', on_delete=models.CASCADE)
    total_amount = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=90, default='pending', choices=choice)
    def __str__(self):
        return str(self.user)




class OrderItem(TimeStampedModel, models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    qty = models.CharField(max_length=5)
    price = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return str(self.order)
