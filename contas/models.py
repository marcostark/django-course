from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_cricao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    observacoes = models.TextField(null=True, blank=True) #Não obrigatorio
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        '''
            Sobrescrever para indicar o plural da classe
        '''
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.descricao