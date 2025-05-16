from django.shortcuts import render

from rest_framework import viewsets
from .models import Categoria, Conteudo
from .serializers import CategoriaSerializer, ConteudoSerializer

class ConteudoViewSet(viewsets.ModelViewSet):
    queryset = Conteudo.objects.all()
    serializer_class = ConteudoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer