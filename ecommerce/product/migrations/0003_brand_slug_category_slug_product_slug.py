# Generated by Django 4.0.3 on 2022-03-27 16:24

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_brand_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title'),
        ),
    ]