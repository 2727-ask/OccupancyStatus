# Generated by Django 3.1.12 on 2022-07-07 08:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0008_hospitalmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HospitalModel',
            new_name='HospitalInformation',
        ),
    ]