# Generated by Django 3.2.5 on 2021-07-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0004_rename_p_category_product_pcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pcategory',
            field=models.CharField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five')], max_length=100, null=True),
        ),
    ]
