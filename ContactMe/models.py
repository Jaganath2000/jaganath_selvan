# models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True)
    contact_email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.contact_number}, {self.contact_email})"
