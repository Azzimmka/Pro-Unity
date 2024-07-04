from django.db import models

from django.db import models

class Registration(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    it = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)



    def __str__(self):
        return self.ism


