# Generated by Django 3.1.4 on 2021-02-14 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
