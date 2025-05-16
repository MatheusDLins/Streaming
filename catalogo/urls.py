from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConteudoViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'conteudos', ConteudoViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]