from django.contrib import admin
from page.models import FILMS, Actor
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.db import models

class FilmAdmin(admin.ModelAdmin):
    pass 


class TutorialAdmin(admin.ModelAdmin):


    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]




admin.site.register(FILMS)
admin.site.register(Actor) # ne pas mettre de S dans les noms de classes

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)
    
