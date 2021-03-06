# Generated by Django 3.1.4 on 2020-12-05 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modelo', '0001_initial'),
        ('marca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('pvp', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='marca.marca')),
                ('modelo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='modelo.modelo')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'db_table': 'producto',
                'ordering': ['-id'],
            },
        ),
    ]
