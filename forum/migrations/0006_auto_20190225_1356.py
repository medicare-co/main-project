# Generated by Django 2.1.2 on 2019-02-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20190222_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=3000),
        ),
    ]
