# Generated by Django 3.2.5 on 2021-08-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0019_auto_20210805_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='razorpay_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]