# Generated by Django 4.1.7 on 2023-03-23 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATCadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employees',
            new_name='auth_user',
        ),
    ]
