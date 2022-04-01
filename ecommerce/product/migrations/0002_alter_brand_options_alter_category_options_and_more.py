# Generated by Django 4.0.3 on 2022-03-27 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'get_latest_by': 'modified'},
        ),
        migrations.RemoveField(
            model_name='brand',
            name='description',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]
