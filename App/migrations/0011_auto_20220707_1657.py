# Generated by Django 3.1.12 on 2022-07-07 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_hospitalsocialinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.hospitalinformation'),
        ),
    ]
