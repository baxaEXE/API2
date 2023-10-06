from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    name = models.CharField(max_length= 256)
    image = models.ImageField()

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class CustomUser(AbstractUser):
    
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username}'