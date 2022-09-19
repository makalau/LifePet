from django.db import models

ESPECIE = [
    ("cachorro", "Cachorro"),
    ("gato", "Gato")
]

PORTE = [
    ("grande", "Grande"),
    ("medio", "Medio"),
    ("pequeno", "Pequeno")
]

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    nascimento = models.CharField(max_length=10)
    email = models.EmailField()
    telefone = models.CharField(max_length=25)
    local = models.CharField(max_length=255)
    numero = models.CharField(max_length=4)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    obs = models.TextField()
    # CAMPO SELECT
    especie = models.CharField(
        max_length=20,
        choices=ESPECIE)
    raca = models.CharField(max_length=20)
    # CAMPO SELECT
    porte = models.CharField(
        max_length=10,
        choices=PORTE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
