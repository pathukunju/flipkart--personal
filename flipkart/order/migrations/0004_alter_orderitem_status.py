# Generated by Django 4.1.2 on 2022-11-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('Order Confirmed', 'Order Confirmed'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery\t'), ('Delivered', 'Delivered')], default='pending', max_length=20),
        ),
    ]