# Generated by Django 5.0 on 2023-12-21 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0002_alter_producto_imagen"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="contenido",
            field=models.CharField(default="Valor predeterminado", max_length=100),
        ),
        migrations.AlterField(
            model_name="categoriaprod",
            name="updated",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="producto",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
