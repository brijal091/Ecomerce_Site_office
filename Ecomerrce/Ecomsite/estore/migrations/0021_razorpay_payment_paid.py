# Generated by Django 3.2.5 on 2021-08-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0020_razorpay_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='razorpay_payment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
