# Generated by Django 4.1.7 on 2023-06-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("livraria", "0007_livros_categoria_livros_editora"),
    ]

    operations = [
        migrations.AddField(
            model_name="livros",
            name="autores",
            field=models.ManyToManyField(related_name="Livros", to="livraria.autor"),
        ),
    ]