from django.db import models

from django.db import models

class Registration(models.Model):
    Имя = models.CharField(max_length=100)
    Фамилия = models.CharField(max_length=100)
    Напровление = models.CharField(max_length=100)
    Телефон = models.CharField(max_length=20)
    # yoshi = models.CharField(max_length=100)


    def __str__(self):
        return self.ism

# Create your models here.
