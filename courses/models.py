from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    # Add more fields as required

    def __str__(self):
        return self.title
