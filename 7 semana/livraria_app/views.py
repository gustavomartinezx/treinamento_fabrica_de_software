from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class LivrariaViewSet(viewsets.ModelViewSet):
    queryset =  Livraria.objects.all()
    serializer_class = LivrariaSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer