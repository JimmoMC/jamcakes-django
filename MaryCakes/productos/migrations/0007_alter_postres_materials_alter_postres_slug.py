# Generated by Django 4.1 on 2022-08-20 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0006_postres_materials_postres_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postres",
            name="materials",
            field=models.TextField(verbose_name="Materiales"),
        ),
        migrations.AlterField(
            model_name="postres", name="slug", field=models.SlugField(max_length=200),
        ),
    ]
