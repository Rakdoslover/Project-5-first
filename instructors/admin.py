from django.contrib import admin
from .models import Instructor

# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sessions',
        'years_of_experience',
        'words_from_the_instructor',
        'image_url',
        'image',
    )

    ordering = ('name',)

admin.site.register(Instructor, InstructorAdmin)
