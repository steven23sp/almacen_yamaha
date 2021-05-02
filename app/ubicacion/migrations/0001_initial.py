# Generated by Django 3.1.4 on 2021-04-01 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estante', '0001_initial'),
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='area.area')),
                ('estante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estante.estante')),
            ],
            options={
                'verbose_name': 'ubicacion',
                'verbose_name_plural': 'ubicacion',
                'db_table': 'ubicacion',
                'ordering': ['-id'],
            },
        ),
    ]
