from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=100);
    genero = models.CharField(max_length=150);
    lancamento = models.DateField()
    
    def __str__(self):
        return self.nome;

class Livraria(models.Model):
    nome = models.CharField(max_length=100);
    endereco = models.CharField(max_length=150);
    tel_para_contato = models.IntegerField(null=True)
    livro = models.ForeignKey(Livro, related_name="livro", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nome;

