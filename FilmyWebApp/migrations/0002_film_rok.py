# Generated by Django 4.0.1 on 2022-01-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmyWebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rok',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
    ]
