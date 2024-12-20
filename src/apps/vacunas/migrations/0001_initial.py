# Generated by Django 5.1.2 on 2024-11-10 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('cant_dosis', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'vacuna',
                'verbose_name_plural': 'vacunas',
                'db_table': 'vacunas',
            },
        ),
        migrations.CreateModel(
            name='Dosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('vacuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dosis_de_vacuna', to='vacunas.vacuna')),
            ],
            options={
                'verbose_name': 'dosis',
                'verbose_name_plural': 'dosis',
                'db_table': 'dosis',
            },
        ),
    ]
