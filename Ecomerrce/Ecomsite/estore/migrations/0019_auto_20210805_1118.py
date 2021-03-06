# Generated by Django 3.2.5 on 2021-08-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0018_remove_product_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(max_length=200, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='Zip',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Zip code'),
        ),
    ]
