from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Editora, Livros, Autor
from livraria.serializers import (
    LivrosDetailSerializer,
    LivrosSerializer,
    LivrosListSerializer,
)


class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()

    serializer_class = {
        "list": LivrosListSerializer,
        "retrieve": LivrosDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, LivrosSerializer)
