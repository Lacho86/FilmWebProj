from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Aktor, Film, DodatkoweInfo, Ocena

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'opis', 'premiera', 'rok', 'imdb_rank', 'plakat']

class DodatkoweInfoForms(ModelForm):
    class Meta:
        model = DodatkoweInfo
        fields = ['czas_trwania', 'gatunek']

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki', 'recenzja']

class AktorForm(ModelForm):
    class Meta:
        model = Aktor
        fields =  ['imie', 'nazwisko']
