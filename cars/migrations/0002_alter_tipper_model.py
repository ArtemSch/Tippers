# Generated by Django 4.0.7 on 2022-11-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipper',
            name='model',
            field=models.CharField(choices=[('belaz', 'Belaz'), ('komatsu', 'Komatsu')], max_length=50),
        ),
    ]
