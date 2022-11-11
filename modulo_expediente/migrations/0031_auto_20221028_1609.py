# Generated by Django 3.2.12 on 2022-10-28 16:09

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modulo_control', '0002_auto_20221028_1602'),
        ('modulo_expediente', '0030_alter_tipoconsulta_nombre'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='paciente',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='brindaconsulta',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.consulta'),
        ),
        migrations.AlterField(
            model_name='brindaconsulta',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_control.doctor'),
        ),
        migrations.AlterField(
            model_name='citaconsulta',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='citaconsulta',
            name='expediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.expediente'),
        ),
        migrations.AlterField(
            model_name='citaconsulta',
            name='horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.horarioconsulta'),
        ),
        migrations.AlterField(
            model_name='constanciamedica',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.consulta'),
        ),
        migrations.AlterField(
            model_name='contieneconsulta',
            name='consulta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.consulta'),
        ),
        migrations.AlterField(
            model_name='contieneconsulta',
            name='expediente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.expediente'),
        ),
        migrations.AlterField(
            model_name='documentoexpediente',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documentoexpediente',
            name='expediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.expediente'),
        ),
        migrations.AlterField(
            model_name='dosis',
            name='medicamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.medicamento'),
        ),
        migrations.AlterField(
            model_name='dosis',
            name='receta_medica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.recetamedica'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dui',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='email_paciente',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento_paciente',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero_telefono',
            field=models.CharField(blank=True, default='', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='pasaporte',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='responsable',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='recetaordenexamenlaboratorio',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.consulta'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='enfermera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
