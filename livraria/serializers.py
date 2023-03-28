from rest_framework.serializers import ModelSerializer
from livraria.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        filds = "__all__"
