# Generated by Django 3.2.5 on 2021-07-30 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0003_product_p_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='p_category',
            new_name='pcategory',
        ),
    ]