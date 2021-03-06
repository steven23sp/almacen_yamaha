# Generated by Django 3.1.4 on 2020-12-06 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compra', '0001_initial'),
        ('producto', '0001_initial'),
        ('inventario', '0002_delete_inventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(default=0, max_length=13, unique=True)),
                ('estado', models.IntegerField(choices=[(1, 'En stock'), (0, 'Vendido')], default=1)),
                ('select', models.IntegerField(choices=[(1, 'Si'), (0, 'No')], default=0)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='compra.compra')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producto.producto')),
            ],
            options={
                'verbose_name': 'inventario',
                'verbose_name_plural': 'inventarios',
                'db_table': 'inventario',
                'ordering': ['-id'],
            },
        ),
    ]
