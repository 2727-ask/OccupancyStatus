# Generated by Django 3.1.12 on 2022-05-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20220522_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='speciality',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
