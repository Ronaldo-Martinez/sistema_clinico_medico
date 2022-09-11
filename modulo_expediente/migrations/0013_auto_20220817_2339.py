# Generated by Django 3.2.12 on 2022-08-17 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0012_alter_contieneconsulta_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='antecedentes_familiares',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='antecedentes_personales',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='contieneconsulta',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='CitaConsulta',
            fields=[
                ('id_cita_consulta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_cita', models.DateTimeField()),
                ('prioridad_paciente', models.CharField(choices=[('1', 'Alta'), ('2', 'Media'), ('3', 'Baja')], max_length=1)),
                ('observacion', models.CharField(blank=True, max_length=80, null=True)),
                ('expediente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modulo_expediente.expediente')),
            ],
        ),
    ]
