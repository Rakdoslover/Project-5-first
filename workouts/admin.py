from django.contrib import admin
from .models import Workout_Session

# Register your models here.

class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'place',
        'price',
        'instructors',
        'image_url',
        'image',
    )

    ordering = ('name',)


admin.site.register(Workout_Session, WorkoutSessionAdmin)
