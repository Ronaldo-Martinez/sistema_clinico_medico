# Generated by Django 3.2.12 on 2022-08-22 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0021_alter_citaconsulta_observacion'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='paciente',
            unique_together={('dui',)},
        ),
    ]