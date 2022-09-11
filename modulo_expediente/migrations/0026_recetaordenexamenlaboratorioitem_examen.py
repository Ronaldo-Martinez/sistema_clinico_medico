# Generated by Django 3.2.12 on 2022-09-05 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_laboratorio', '0002_ordenexamenlaboratorio_ordenexamenlaboratorioitem'),
        ('modulo_expediente', '0025_remove_recetaordenexamenlaboratorioitem_examen_de_laboratorio'),
    ]

    operations = [
        migrations.AddField(
            model_name='recetaordenexamenlaboratorioitem',
            name='examen',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='modulo_laboratorio.examenlaboratorio'),
            preserve_default=False,
        ),
    ]
