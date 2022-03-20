from django.db import models

# Create your models here.


class Miku(models.Model):
    x = models.DecimalField(max_digits=5, decimal_places=0)
