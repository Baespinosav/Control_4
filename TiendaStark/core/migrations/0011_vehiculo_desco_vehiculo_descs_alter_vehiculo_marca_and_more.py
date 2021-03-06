# Generated by Django 4.0.5 on 2022-06-25 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_categoriaproducto_manbod_manproducto_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='desco',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Descuento Oferta'),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='descs',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Descuento Susciptor'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(max_length=80, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='modelo',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Nombre Producto'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='patente',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
