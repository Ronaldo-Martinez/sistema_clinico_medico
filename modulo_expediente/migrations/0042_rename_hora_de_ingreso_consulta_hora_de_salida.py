# Generated by Django 3.2.12 on 2023-05-14 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0041_auto_20230514_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='hora_de_ingreso',
            new_name='hora_de_salida',
        ),
    ]