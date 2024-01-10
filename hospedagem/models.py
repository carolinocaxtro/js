from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf= models.IntegerField()
    data_entrada= models.DateField()
    data_saida= models.DateField()

class IDCliente(models.Model):
    id_cliente= models.ForeignKey(Cliente,on_delete=models.CASCADE)




