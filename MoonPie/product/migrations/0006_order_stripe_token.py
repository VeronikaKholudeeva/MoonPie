# Generated by Django 3.1.6 on 2022-05-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_token',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
