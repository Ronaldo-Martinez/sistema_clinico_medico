# Generated by Django 3.2.12 on 2022-08-17 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0013_auto_20220817_2153'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contieneconsulta',
            unique_together={('expediente', 'fecha_de_cola')},
        ),
    ]
