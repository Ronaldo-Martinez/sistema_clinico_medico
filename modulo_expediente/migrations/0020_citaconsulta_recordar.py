# Generated by Django 3.2.12 on 2022-08-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0019_recetamedica_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='citaconsulta',
            name='recordar',
            field=models.BooleanField(default=False),
        ),
    ]
