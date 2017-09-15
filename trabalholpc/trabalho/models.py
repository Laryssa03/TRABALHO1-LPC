from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome=models.CharField (max_length = 150)
    email=models.CharField (max_length = 150)

    def __str__(self):
        return self.nome
class PessoaFisica(Pessoa):
    cpf= models.CharField (max_length = 12)
    
    def __str__(self):
        return self.cpf
class PessoaJuridica(Pessoa):
    cnpj=models.CharField (max_length = 50)
    razaosocial=models.CharField (max_length = 150)

    def __str__(self):
        return self.razaosocial


    def __str__(self):
        return self.curriculo
    
    



class Evento(models.Model):
    nome = models.CharField (max_length = 150)
    eventoPrincipal = models.CharField (max_length = 150)
    sigla = models.CharField (max_length = 10)
    dataEHoraDeInicio = models.DateTimeField(blank=True,null= True)
    palavrasChave = models.CharField (max_length = 150)
    logotipo = models.CharField (max_length = 10)
    realizador = models.ForeignKey(Pessoa, null=True, blank=False)
    cidade =models.CharField (max_length = 100)
    uf=models.CharField (max_length = 2)
    endereço=models.CharField (max_length = 250)
    cep=models.CharField (max_length = 10)

    def __str__(self):
        return self.nome

class EventoCientifico(Evento):
    issn=models.CharField (max_length = 150)
    def __str__(self):
        return self.issn

class ArtigoCientifico(models.Model):
    titulo=models.CharField (max_length = 150)
    evento= models.ForeignKey(EventoCientifico, null=True, blank=False)
    def __str__(self):
        return self.titulo
class Autor(Pessoa):
    curriculo=models.CharField (max_length = 150)
    artigos=models.ManyToManyField(ArtigoCientifico,blank=True)