# Generated by Django 4.2.7 on 2023-12-04 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_carrito_isopen_carritoproductos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='id_producto',
        ),
    ]
