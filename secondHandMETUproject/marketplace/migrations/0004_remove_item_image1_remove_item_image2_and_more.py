# Generated by Django 5.0 on 2023-12-12 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_rename_image_item_image1_item_image2_item_image3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image5',
        ),
    ]
