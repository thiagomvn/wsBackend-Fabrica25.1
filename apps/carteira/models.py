from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    rate = models.FloatField()

    def __str__(self):
        return self.code