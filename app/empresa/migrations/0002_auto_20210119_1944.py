# Generated by Django 3.1.4 on 2021-01-20 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='indice',
            field=models.DecimalField(decimal_places=2, default=0.25, max_digits=9),
        ),
    ]
