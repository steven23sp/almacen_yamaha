# Generated by Django 3.1.4 on 2021-01-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='edad',
            field=models.IntegerField(default=18),
        ),
    ]
