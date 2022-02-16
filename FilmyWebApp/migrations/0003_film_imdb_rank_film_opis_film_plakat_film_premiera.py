# Generated by Django 4.0.1 on 2022-01-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmyWebApp', '0002_film_rok'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imdb_rank',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='opis',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='film',
            name='plakat',
            field=models.ImageField(blank=True, null=True, upload_to='plakaty'),
        ),
        migrations.AddField(
            model_name='film',
            name='premiera',
            field=models.DateField(blank=True, null=True),
        ),
    ]
