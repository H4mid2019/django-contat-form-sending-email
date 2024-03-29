# Generated by Django 2.2.5 on 2019-10-15 15:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=128, validators=[django.core.validators.EmailValidator(message='Please, enter corresponding email address')])),
                ('comment', models.TextField(max_length=250)),
                ('user_info', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
