# Generated by Django 3.1.4 on 2021-05-01 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_remove_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='producto/imagen', verbose_name='Imagen'),
        ),
    ]
