# Generated by Django 3.1.12 on 2022-06-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_hospital_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]