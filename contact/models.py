from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    #forms do contatono admin django
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    # salvar o nome do contato na lista, ao inves de "Contact Object (id)"
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

