from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria, Editora, Livros, Autor

class LivrosSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = "__all__"


class LivrosDetailSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = "__all__"
        depth = 1

class LivrosListSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = ["id", "titulo", "preco"]
