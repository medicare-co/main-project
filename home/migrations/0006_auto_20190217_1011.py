# Generated by Django 2.1.2 on 2019-02-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190217_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
