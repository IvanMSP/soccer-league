from django.db import models
from teams.models import Team


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
    nationality = models.CharField(max_length=25, blank=True, null=True)
    stature = models.CharField(max_length=10, blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    sex = models.CharField(
        max_length=15,
        choices=SEX_CHOICES,
        default='Masculino'
    )
    team_player = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)
    number = models.IntegerField()
    postion = models.CharField(
        max_length=30,
        choices=PLAYER_POSTIONS_CHOINCES,
        default='Ninguna'
    )

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
    
    def __str__(self):
        return self.name.title()