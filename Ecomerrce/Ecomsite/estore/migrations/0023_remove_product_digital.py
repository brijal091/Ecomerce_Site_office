# Generated by Django 3.2.5 on 2021-08-11 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0022_cupon_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
