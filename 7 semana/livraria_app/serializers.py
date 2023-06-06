from .models import *
from rest_framework import serializers



class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ["id", "nome", "genero", "lancamento"]

class LivrariaSerializer(serializers.ModelSerializer):
    livro = serializers.SlugRelatedField(
        many=False,
        slug_field="nome",
        read_only=False,
        queryset=Livro.objects.all(),
    )
    class Meta:
        model = Livraria
        fields = "__all__"