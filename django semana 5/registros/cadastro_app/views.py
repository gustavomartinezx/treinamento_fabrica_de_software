from rest_framework import viewsets
from cadastro_app.serializers import CadastroSerializer
from cadastro_app.models import Cadastro

class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer