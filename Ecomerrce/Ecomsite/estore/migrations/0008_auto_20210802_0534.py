# Generated by Django 3.2.5 on 2021-08-02 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0007_auto_20210802_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
