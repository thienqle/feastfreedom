# Generated by Django 2.1.3 on 2018-11-28 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='kit_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen', to='service_provider.Kitchen'),
        ),
    ]
