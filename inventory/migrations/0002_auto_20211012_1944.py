# Generated by Django 3.1 on 2021-10-12 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(max_length=20, verbose_name='Código de Barra'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Costo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio'),
        ),
    ]
