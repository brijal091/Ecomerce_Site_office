# Generated by Django 3.2.5 on 2021-08-03 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0013_auto_20210802_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Upload Product Image'),
        ),
    ]