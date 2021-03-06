# Generated by Django 4.0.1 on 2022-02-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmyWebApp', '0006_alter_dodatkoweinfo_gatunek_aktor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktor',
            name='filmy',
            field=models.ManyToManyField(related_name='aktorzy', to='FilmyWebApp.Film'),
        ),
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Komedia'), (1, 'Horror'), (0, 'Inne'), (3, 'Sci-fi'), (4, 'Dramat')], default=0),
        ),
    ]
