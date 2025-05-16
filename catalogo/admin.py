from django.contrib import admin
from .models import Conteudo, Categoria

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'categoria', 'data_lancamento', 'disponivel')
    list_filter = ('tipo', 'categoria')
    search_fields = ('titulo',)

admin.site.register(Categoria)