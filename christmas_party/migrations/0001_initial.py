# Generated by Django 5.0.7 on 2024-07-11 13:37

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, unique=True)),
                ('company', models.CharField(choices=[('wesupport incorporated', 'WeSupport Incorporated '), ('tranzend solutions and trading corporation', 'Tranzend Solutions and Trading Corporation'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=100)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=11, region='PH')),
                ('coupon', models.CharField(max_length=255)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['create_timestamp'],
            },
        ),
    ]
