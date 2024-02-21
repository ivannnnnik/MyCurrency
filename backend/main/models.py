from django.db import models, connection


class Currency(models.Model):
    """
    name - name of the currency
    rate - rate of the currency
    """

    name = models.CharField(max_length=256, unique=True)
    rate = models.FloatField()

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

    def __str__(self):
        return f"{self.name}"
