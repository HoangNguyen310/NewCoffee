# Generated by Django 2.2.1 on 2019-05-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='address',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
