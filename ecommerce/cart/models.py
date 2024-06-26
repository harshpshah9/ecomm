from django.db import models
from user.models import User
from product.models import Product
from base.base import BaseModel
from django_extensions.db.models import *


# Create your models here.
class Cart(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    @property
    def total_amount(self):
        return self.qty * self.product.price
