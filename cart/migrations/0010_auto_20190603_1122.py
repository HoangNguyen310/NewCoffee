# Generated by Django 2.2.1 on 2019-06-03 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]