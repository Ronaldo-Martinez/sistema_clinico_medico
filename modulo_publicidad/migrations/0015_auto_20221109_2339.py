# Generated by Django 3.2.12 on 2022-11-09 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_publicidad', '0014_auto_20221026_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id_visita', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cantidad_visitas', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='descuento',
            name='servicio',
        ),
        migrations.AddField(
            model_name='descuento',
            name='publicacion',
            field=models.OneToOneField(default=63, on_delete=django.db.models.deletion.CASCADE, related_name='descuentos', to='modulo_publicidad.publicacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='cantidad_visitas',
            field=models.IntegerField(default=0),
        ),
    ]
