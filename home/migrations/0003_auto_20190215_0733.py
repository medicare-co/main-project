# Generated by Django 2.1.2 on 2019-02-15 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contents', models.TextField(max_length=2000)),
                ('date', models.DateField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='buyer',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
