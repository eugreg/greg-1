from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria,Editora,Livros, Autor
from livraria.serializers import CategoriaSerializer,EditoraSerializer, AutorSerializer, LivrosDetailSerializer, LivrosSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    

    def get_serializer_class(self):
        if self.action in ["list", "retrive"]:
            return LivrosDetailSerializer
        return LivrosSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer



class EditoraViewset(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
