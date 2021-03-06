# Generated by Django 3.1.4 on 2020-12-06 03:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo_gasto', '0001_initial'),
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('detalle', models.CharField(max_length=50)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresa.empresa')),
                ('tipo_gasto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tipo_gasto.tipo_gasto')),
            ],
            options={
                'verbose_name': 'gasto',
                'verbose_name_plural': 'gastos',
                'db_table': 'gasto',
                'ordering': ['-id', '-tipo_gasto', '-valor'],
            },
        ),
    ]
