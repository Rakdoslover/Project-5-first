from django.db import models
from instructors.models import Instructor


class Workout_Session(models.Model):
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    place = models.TextField(default="Anywhere")
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    instructors = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
