# Generated by Django 2.2.1 on 2019-05-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20190522_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product/'),
        ),
    ]