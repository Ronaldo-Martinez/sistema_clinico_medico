# Generated by Django 3.2.12 on 2022-08-18 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0014_citaconsulta_empleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioConsulta',
            fields=[
                ('id_horario', models.AutoField(primary_key=True, serialize=False)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
    ]
