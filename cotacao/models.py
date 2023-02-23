from django.db import models

# Create your models here.
class Produto(models.Model):
	descricao = models.CharField(max_length=30)
	categoria = models.CharField(max_length=30)
	valor = models.CharField(max_length=10)

