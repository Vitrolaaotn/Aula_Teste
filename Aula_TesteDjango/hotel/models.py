from django.db import models
import datetime

# Create your models here.

TIPOS_QUARTOS = (
    ('SOLTEIRO', "Solteiro"),
    ('CASAL', 'Casal'),
    ('CONFORT', 'Confort'),
    ('LUXO', 'Luxo'),
)

class hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to='logos/', )

    def __str__(self):
        return self.titulo

class quarto(models.Model):
    tipo = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length=9999)
    descricao = models.TextField (max_length=255)
    foto_quarto = models.ImageField(upload_to='foto_quartos/' )

    def __str__(self):
        return self.titulo