# Generated by Django 3.2.12 on 2023-05-14 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0044_auto_20230514_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='hora_de_entrada',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
