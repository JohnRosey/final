# Generated by Django 2.1.5 on 2021-11-27 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noyau', '0003_auto_20211127_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netfeelex',
            name='Date_publie',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 19, 28, 57, 266231), verbose_name='Date publié'),
        ),
    ]
