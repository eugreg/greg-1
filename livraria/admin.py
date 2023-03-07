from django.contrib import admin

from .models import Categoria, Editora, Autor, Livros              

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livros)
