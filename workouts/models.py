from django.db import models
from instructors.models import Instructor


class Workout_Session(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    place = models.TextField()
    instructors = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
