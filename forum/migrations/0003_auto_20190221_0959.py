# Generated by Django 2.1.2 on 2019-02-21 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20190221_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]