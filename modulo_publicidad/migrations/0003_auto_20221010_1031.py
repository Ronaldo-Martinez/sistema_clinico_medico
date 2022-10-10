# Generated by Django 3.2.12 on 2022-10-10 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0030_alter_tipoconsulta_nombre'),
        ('modulo_laboratorio', '0007_auto_20221010_0031'),
        ('modulo_publicidad', '0002_auto_20221010_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciolaboratorioclinico',
            name='examen_laboratorio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.examenlaboratorio'),
        ),
        migrations.AlterField(
            model_name='serviciolaboratorioclinico',
            name='servicio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='servicios_laboratorio_clinico', to='modulo_publicidad.servicio'),
        ),
        migrations.AlterField(
            model_name='serviciomedico',
            name='servicio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='servicios_medicos', to='modulo_publicidad.servicio'),
        ),
        migrations.AlterField(
            model_name='serviciomedico',
            name='tipo_consulta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.tipoconsulta'),
        ),
    ]