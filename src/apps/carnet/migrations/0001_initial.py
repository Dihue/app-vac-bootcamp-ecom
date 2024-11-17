# Generated by Django 5.1.2 on 2024-11-17 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0003_alter_paciente_apellido_alter_paciente_genero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarnetVacunacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
    ]
