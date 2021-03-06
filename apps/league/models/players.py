from django.db import models
from .teams import Team
#reusable apps
from reusable.constants import *


PLAYER_POSTIONS_CHOINCES = (
    ('portero', 'Portero'),
    ('defensa', 'Defensa'),
    ('medio', 'Medio'),
    ('delantero', 'Delantero')
)

SEX_CHOICES = (
    ('femenino', 'Femenino'),
    ('masculino', 'Masculino'),
)


class Player(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    nationality = models.CharField(max_length=25, **NULL)
    stature = models.CharField(max_length=10, **NULL)
    weight = models.CharField(max_length=10, **NULL)
    number = models.IntegerField()
    sex = models.CharField(
        max_length=15,
        choices=SEX_CHOICES,
        default='Masculino'
    )
    postion = models.CharField(
        max_length=30,
        choices=PLAYER_POSTIONS_CHOINCES,
        default='Ninguna'
    )
    picture = models.ImageField(
        upload_to='players/picture/',
        max_length=1000,
        blank=True, 
        null=True
    )
    team_player = models.ForeignKey(
        Team, 
        related_name='jugadores',
        **NULL, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
    
    def __str__(self):
        return self.name.title()