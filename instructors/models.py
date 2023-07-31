from django.db import models


class Instructor(models.Model):
    """ main instructors model """
    name = models.CharField(max_length=254)
    sessions = models.TextField()
    years_of_experience = models.IntegerField(default=0)
    words_from_the_instructor = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
