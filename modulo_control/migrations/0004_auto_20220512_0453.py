# Generated by Django 3.2.12 on 2022-05-12 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_control', '0003_auto_20220510_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='Empleado',
            new_name='empleado',
        ),
        migrations.RemoveField(
            model_name='liclaboratorioclinico',
            name='jvmp',
        ),
        migrations.AddField(
            model_name='liclaboratorioclinico',
            name='empleado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='modulo_control.empleado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='liclaboratorioclinico',
            name='jvplc',
            field=models.IntegerField(default=0),
        ),
    ]
