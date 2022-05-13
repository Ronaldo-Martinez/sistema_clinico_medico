# Generated by Django 3.2.12 on 2022-05-06 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0003_auto_20220503_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='diagnostico',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='examen_de_laboratorio',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='modulo_expediente.ordenexamenlaboratorio'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='sintoma',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
