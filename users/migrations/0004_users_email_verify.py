# Generated by Django 4.1.3 on 2022-11-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_alter_users_managers_alter_users_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
    ]
