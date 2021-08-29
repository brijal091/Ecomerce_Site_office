# Generated by Django 3.2.5 on 2021-08-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0021_razorpay_payment_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('discount', models.IntegerField(null=True)),
                ('status', models.BooleanField(default=False, verbose_name='Activate')),
            ],
        ),
    ]
