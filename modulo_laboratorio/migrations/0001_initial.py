# Generated by Django 3.2.12 on 2022-08-02 04:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulo_expediente', '0001_initial'),
        ('modulo_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_categoria', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaExamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ExamenLaboratorio',
            fields=[
                ('id_examen_laboratorio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_examen', models.CharField(max_length=40)),
                ('tipo_muestra', models.CharField(blank=True, choices=[('NA', ''), ('1', 'sangre'), ('2', 'orina'), ('3', 'heces'), ('4', 'tejidos')], default='NA', max_length=15)),
                ('nota', models.CharField(blank=True, default='', max_length=100)),
                ('categoria', models.ManyToManyField(through='modulo_laboratorio.CategoriaExamen', to='modulo_laboratorio.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id_parametro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_parametro', models.CharField(max_length=40)),
                ('unidad_parametro', models.CharField(blank=True, max_length=40, null=True)),
                ('valor_por_defecto', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('examen_de_laboratorio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.examenlaboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='ServicioDeLaboratorioClinico',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('precio_servicio_clinica', models.DecimalField(decimal_places=2, max_digits=10)),
                ('examen_de_laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.examenlaboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id_resultado', models.AutoField(primary_key=True, serialize=False)),
                ('observaciones', models.TextField(blank=True, default='')),
                ('fecha_hora_toma_de_muestra', models.DateTimeField(blank=True, null=True)),
                ('fecha_hora_elaboracion_de_reporte', models.DateTimeField(blank=True, null=True)),
                ('examen_laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.examenlaboratorio')),
                ('lic_laboratorio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulo_control.liclaboratorioclinico')),
            ],
        ),
        migrations.CreateModel(
            name='RangoDeReferencia',
            fields=[
                ('id_rango_referencia', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, default='', max_length=75)),
                ('valor_maximo', models.CharField(blank=True, max_length=15, null=True)),
                ('valor_minimo', models.CharField(blank=True, max_length=15, null=True)),
                ('valor', models.CharField(blank=True, max_length=15, null=True)),
                ('unidad', models.CharField(blank=True, default='', max_length=8)),
                ('parametro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.parametro')),
            ],
        ),
        migrations.CreateModel(
            name='EsperaExamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_pago_laboratorio', models.CharField(choices=[('1', 'Cancelado'), ('3', 'Pendiente')], default='3', max_length=15)),
                ('numero_cola_laboratorio', models.IntegerField()),
                ('consumo_laboratorio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fase_examenes_lab', models.CharField(choices=[('1', 'Recepción de muestra'), ('2', 'Resultados en Proceso'), ('3', 'Resultados Listos'), ('4', 'Resultados Entregado'), ('5', 'Proceso Finalizado')], default='1', max_length=25)),
                ('fecha', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('expediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_expediente.expediente')),
                ('resultado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.resultado')),
            ],
        ),
        migrations.AddField(
            model_name='categoriaexamen',
            name='examen_laboratorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.examenlaboratorio'),
        ),
        migrations.CreateModel(
            name='ContieneValor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dato', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('parametro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.parametro')),
                ('resultado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_laboratorio.resultado')),
            ],
            options={
                'unique_together': {('resultado', 'parametro')},
            },
        ),
    ]
