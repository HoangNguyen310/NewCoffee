# Generated by Django 2.2.1 on 2019-05-15 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/img/uploads'),
        ),
    ]
