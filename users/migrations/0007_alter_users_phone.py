# Generated by Django 4.1.3 on 2022-11-18 13:57

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=phone_field.models.PhoneField(default='123', max_length=31, unique=True),
            preserve_default=False,
        ),
    ]
