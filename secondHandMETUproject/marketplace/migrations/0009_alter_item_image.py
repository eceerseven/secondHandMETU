# Generated by Django 5.0 on 2023-12-13 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0008_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='secondHandMETU\\secondHandMETUproject\\static\\images'),
        ),
    ]
