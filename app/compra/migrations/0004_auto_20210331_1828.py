# Generated by Django 3.1.4 on 2021-03-31 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0003_compra_inventario_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='inventario_estado',
            field=models.IntegerField(choices=[(0, 'NO'), (1, 'SI')], default=0),
        ),
    ]
