# Generated by Django 3.2.12 on 2022-06-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_laboratorio', '0014_auto_20220608_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenlaboratorio',
            name='nota',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
