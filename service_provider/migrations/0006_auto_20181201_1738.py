# Generated by Django 2.1.3 on 2018-12-01 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0005_auto_20181128_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='email',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='password',
        ),
    ]