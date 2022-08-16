from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.models.IntegerField()
    rendimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})