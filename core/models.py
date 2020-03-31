from django.db import models
import datetime

class Entry(models.Model):
    date = models.DateField(default=datetime.date.today)
    value = models.IntegerField()

class Formula(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    confirmed = models.ManyToManyField(Entry, related_name="%(class)s_confirmed")
    confirmed_formula = models.ForeignKey(Formula, on_delete=models.CASCADE, null=True, related_name="%(class)s_country_confirmed")
    death = models.ManyToManyField(Entry, related_name="%(class)s_death")
    death_formula = models.ForeignKey(Formula, on_delete=models.CASCADE, null=True, related_name="%(class)s_country_death")
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)