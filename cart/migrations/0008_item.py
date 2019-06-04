# Generated by Django 2.2.1 on 2019-06-03 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20190601_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]