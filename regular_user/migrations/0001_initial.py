# Generated by Django 2.1.3 on 2018-11-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegularUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(blank=True, null=True)),
                ('lname', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('ques1', models.TextField(blank=True, null=True)),
                ('ans1', models.TextField(blank=True, null=True)),
                ('ques2', models.TextField(blank=True, null=True)),
                ('ans2', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
