# Generated by Django 3.1.12 on 2022-07-07 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20220707_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.hospitalinformation'),
        ),
    ]
