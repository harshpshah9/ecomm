# Generated by Django 4.0.3 on 2022-04-10 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_productcoupon_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='product',
        ),
    ]