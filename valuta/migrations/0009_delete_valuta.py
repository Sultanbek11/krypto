# Generated by Django 4.1.3 on 2022-12-03 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_account_count_valutes'),
        ('valuta', '0008_remove_value_valut_value_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Valuta',
        ),
    ]