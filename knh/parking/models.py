from django.db import models

class Spot(models.Model):
    id = models.IntegerField(primary_key=True)
    occupied = models.BooleanField()
    owner = models.CharField(max_length=255)
    dateFrom = models.CharField(max_length=255)
    nOfDays = models.IntegerField()
    def __str__(self):
        if self.occupied:
            return f'{self.id} - foglalt - {self.owner}'
        else:
            return f'{self.id} - szabad - {self.owner}'