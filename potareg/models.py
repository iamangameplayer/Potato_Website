from django.db import models

class Pota(models.Model):

    PotaSize = models.CharField(max_length=200)
    PotaCost = models.IntegerField()
    PotaBirth = models.DateField()
    PotaName  = models.CharField(max_length=200)

