# Generated by Django 3.2.12 on 2022-05-14 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_control', '0004_auto_20220512_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='roles',
        ),
        migrations.AddField(
            model_name='empleado',
            name='roles',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.DO_NOTHING, to='modulo_control.rol'),
            preserve_default=False,
        ),
    ]