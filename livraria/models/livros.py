from django.db import models

from livraria.models import Categoria, Editora,  Autor

class Livros(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=23, null=True, blank=True)
    quantidade = models.IntegerField(default=0)
    autores = models.ManyToManyField(Autor, related_name="Livros")
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"

    class Meta:
        verbose_name_plural = "Livros"
