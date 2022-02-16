from dataclasses import field
from django.contrib import admin
from .models import Aktor, DodatkoweInfo, Film, Ocena

# admin.site.register(Film)
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis"]
    # exclude = ["opis"]
    list_display = ["tytul", "imdb_rank", "rok"]
    list_filter = ("tytul",)
    search_fields = ("tytul", "opis")

admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)