# Generated by Django 3.1.12 on 2022-07-07 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_auto_20220707_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.hospitalinformation')),
            ],
        ),
    ]
