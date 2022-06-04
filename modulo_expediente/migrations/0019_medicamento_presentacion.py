# Generated by Django 3.2.12 on 2022-05-30 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_expediente', '0018_auto_20220528_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='presentacion',
            field=models.CharField(choices=[(1, 'Frasco'), (2, 'Ampolla'), (3, 'Frasco vial'), (4, 'Sobre'), (5, 'Jeringa prellenada'), (6, 'Bolsa'), (7, 'Tubo'), (8, 'Tarro'), (9, 'Dispositivo precargado'), (10, 'Pluma multidosis'), (11, 'Cartucho'), (12, 'Frasco gotero'), (13, 'Capsulas'), (14, 'Spray'), (15, 'Suspensión')], default=13, max_length=25),
        ),
    ]