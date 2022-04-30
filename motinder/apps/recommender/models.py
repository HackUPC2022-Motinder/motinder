from django.db import models


class Motorcycle(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand_id = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()
    fuel = models.IntegerField()
    price = models.FloatField()
    elo = models.IntegerField()
    probability_price_low = models.FloatField()
    probability_price_medium = models.FloatField()
    probability_price_high = models.FloatField()
    probability_price_low = models.FloatField()

    class Meta:
        verbose_name = 'Motorcycle'
        verbose_name_plural = 'Motorcycles'

    REQUIRED_FIELDS = ['name', 'brand_id', 'year', 'fuel', 'price']

    def __str__(self):
        return f'{self.name} {self.last_name}'
