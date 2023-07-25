from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.serializers import ImageSerializer
from uploader.models import Image
from livraria.models import Livros


class LivrosSerializer(ModelSerializer):
    class Meta:
        capa_attachement_key = SlugRelatedField(
            source="capa",
            slug_field="attachment_key",
            queryset=Image.objects.all(),
            required=False,
            write_only=True,
        )
        capa= ImageSerializer(required=False, read_only=True)
        model = Livros
        fields = "__all__"


class LivrosDetailSerializer(ModelSerializer):
    class Meta:
        model = Livros
        capa= ImageSerializer(required=False)
        fields = "__all__"
        depth = 1


class LivrosListSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = ["id", "titulo", "preco"]
