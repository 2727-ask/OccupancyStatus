# Generated by Django 3.1.12 on 2022-06-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
