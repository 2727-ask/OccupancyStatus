# Generated by Django 3.1.12 on 2022-06-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20220602_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
