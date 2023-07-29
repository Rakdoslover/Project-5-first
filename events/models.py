from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.timezone import now


STATUS = ((0, "Draft"), (1, "Published"))


# Events for the event page (event model)
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(default=now, editable=True, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, default=now)
    location = models.TextField(default='Work Workouts Gym')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
