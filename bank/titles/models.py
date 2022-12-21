from django.db import models

TITLE_ID_CHOICES = [
    ("USD", "USD"),
    ("TRPV", "TRPV"),
    ("TP", "TP"),
    ("TID", "TID"),
    ("THI", "THI"),
    ("TESU", "TESU"),
    ("TEST", "TEST"),
    ("TESP", "TESP"),
    ("TESOROS", "TESOROS"),
    ("TESI", "TESI"),
]
TITLE = [
    ("DOLAR", "DOLAR"),
    (
        "TÍTULO DE PARTICIPACIÓN RENTA VARIABLE",
        "TÍTULO DE PARTICIPACIÓN RENTA VARIABLE",
    ),
    ("TITULO DE PARTICIPACIÓN", "TITULO DE PARTICIPACIÓN"),
    ("TIDIS", "TIDIS"),
    ("TITULOS HIPOTECARIOS", "TITULOS HIPOTECARIOS"),
    ("TES UVR", "TES UVR"),
    ("TES TRM", "TES TRM"),
    ("TES PESOS", "TES PESOS"),
    ("BONOS DEL TESORO EEUU", "BONOS DEL TESORO EEUU"),
    ("TES IPC", "TES IPC"),
]
FEE_CHOICES = [("y", "y"), ("n", "n")]


class Title(models.Model):
    title_id = models.CharField(max_length=20, unique=True, choices=TITLE_ID_CHOICES)
    title = models.CharField(max_length=50, choices=TITLE)
    clasification = models.CharField(max_length=30, blank=True, null=True)
    value = models.CharField(max_length=30)
    creation_date = models.DateField()
    expiration_date = models.DateField()
    fee_paid = models.CharField(max_length=20, choices=FEE_CHOICES)
