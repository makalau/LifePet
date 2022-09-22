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
    nascimento = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=25)
    local = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=4, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    # CAMPO SELECT
    especie = models.CharField(
        max_length=20,
        choices=ESPECIE)
    raca = models.CharField(max_length=20, blank=True, null=True)
    # CAMPO SELECT
    porte = models.CharField(
        max_length=10,
        choices=PORTE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.nome