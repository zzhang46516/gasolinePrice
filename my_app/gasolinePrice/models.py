from django.db import models


class States(models.Model):
    states = models.CharField(max_length=15, default=None, unique=True)

    def __str__(self):
        return self.states


class UpdatePrice(models.Model):
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    release_date = models.DateField(max_length=20)
    price = models.DecimalField(decimal_places=3, max_digits=100)

    def __str__(self):
        return self.state.states


