from django.db import models

# Create your models here.
from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    # Add more fields as required

    def __str__(self):
        return self.name
