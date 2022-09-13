# Generated by Django 3.2.12 on 2022-09-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_laboratorio', '0002_ordenexamenlaboratorio_ordenexamenlaboratorioitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenexamenlaboratorioitem',
            name='orden_examen_laboratorio',
        ),
        migrations.RemoveField(
            model_name='ordenexamenlaboratorioitem',
            name='resultado',
        ),
        migrations.RemoveField(
            model_name='serviciodelaboratorioclinico',
            name='examen_de_laboratorio',
        ),
        migrations.RenameField(
            model_name='esperaexamen',
            old_name='numero_cola_laboratorio',
            new_name='numero_cola_orden',
        ),
        migrations.RemoveField(
            model_name='esperaexamen',
            name='consumo_laboratorio',
        ),
        migrations.RemoveField(
            model_name='esperaexamen',
            name='resultado',
        ),
        migrations.AddField(
            model_name='resultado',
            name='fase_examenes_lab',
            field=models.CharField(choices=[('1', 'Recepción de muestra'), ('2', 'Resultados en Proceso'), ('3', 'Resultados Listos')], default='1', max_length=25),
        ),
        migrations.AddField(
            model_name='resultado',
            name='numero_cola_resultado',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='esperaexamen',
            name='fase_examenes_lab',
            field=models.CharField(choices=[('RC', 'Recepcion'), ('EP', 'En Proceso'), ('RE', 'Resultados Entregado'), ('PF', 'Proceso Finalizado')], default='RC', max_length=2),
        ),
        migrations.DeleteModel(
            name='OrdenExamenLaboratorio',
        ),
        migrations.DeleteModel(
            name='OrdenExamenLaboratorioItem',
        ),
        migrations.DeleteModel(
            name='ServicioDeLaboratorioClinico',
        ),
    ]
