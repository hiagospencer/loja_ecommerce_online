from django.db import models
from django.utils import timezone


LISTA_CATEGORIA = (
    ('fones', 'Fones de Ouvidos'),
    ('caixa de som', 'Caixa de Som'),
    ('receptor', 'Receptores'), 
    ('controles', 'Controles'),
    ('acessorios', 'Acessorios'),
    ('video games', 'Video Games e Jogos'),
)

class Produto(models.Model):
    produto = models.CharField(max_length=30)
    detalhe_produto = models.TextField(max_length=2000)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=1000000)
    imagem = models.ImageField(upload_to='img')
    data_produto = models.DateTimeField(default=timezone.now)
    stoque = models.IntegerField()
    categoria = models.CharField(max_length=30, choices=LISTA_CATEGORIA)

    def __str__(self):
        return self.produto