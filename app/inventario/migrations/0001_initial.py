# Generated by Django 3.1.4 on 2020-12-06 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compra', '0001_initial'),
        ('producto', '0001_initial'),
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_ingreso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='compra.compra')),
                ('fecha_salida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='venta.venta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producto.producto')),
            ],
            options={
                'verbose_name': 'inventario',
                'verbose_name_plural': 'inventarios',
                'db_table': 'inventario',
            },
        ),
    ]
