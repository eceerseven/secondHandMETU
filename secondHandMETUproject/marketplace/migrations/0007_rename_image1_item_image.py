# Generated by Django 5.0 on 2023-12-12 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_rename_image_item_image1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image1',
            new_name='image',
        ),
    ]
