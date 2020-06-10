from django.contrib import admin
from page.models import FILMS, ACTEURS

class FilmAdmin(admin.ModelAdmin):
    pass 

admin.site.register(FILMS)
admin.site.register(ACTEURS) # ne pas mettre de S dans les noms de classes