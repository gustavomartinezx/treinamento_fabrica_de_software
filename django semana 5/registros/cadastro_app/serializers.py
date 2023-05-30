from rest_framework import serializers
from cadastro_app.models import Cadastro


class CadastroSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Cadastro
        fields = ["id", "nome", "nascimento", "cidade", "senha", "email"]