# Generated by Django 3.2.12 on 2022-05-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='id_expediente',
        ),
        migrations.AddField(
            model_name='expediente',
            name='id_paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.paciente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='responsable',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo_paciente',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1),
        ),
    ]