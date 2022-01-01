# Generated by Django 3.2.10 on 2022-01-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20220101_0730'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='cart',
            name='cart_cart_payment_01ed52_idx',
        ),
        migrations.AddIndex(
            model_name='cart',
            index=models.Index(fields=['uuid', 'payment_type'], name='cart_cart_uuid_77f1c8_idx'),
        ),
    ]
