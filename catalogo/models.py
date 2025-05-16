from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return super().__str__()
    
class Conteudo(models.Model):
    TIPOS = [
        ('F', 'Filme'),
        ('S', 'Série')

    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo = models.CharField(max_length=1, choices=TIPOS)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_lancamento = models.DateField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo