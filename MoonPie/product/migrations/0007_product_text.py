# Generated by Django 3.1.6 on 2022-05-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_order_stripe_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
