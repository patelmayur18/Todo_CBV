from django.db import models
from django.shortcuts import reverse
# Create your models here.


class todo(models.Model):
    event = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.event
