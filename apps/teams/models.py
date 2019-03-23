from django.db import models
from league.models import Stadium, League


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    fb_id = models.CharField(max_length=50, blank=True, null=True)
    picture = models.ImageField(
        upload_to='teams/picture/',
        max_length=1000,
        blank=True, 
        null=True
    )
    stadium_team = models.ForeignKey(
        Stadium,
        related_name='equipos_stadium',
        blank=True, null=True,
        on_delete=models.CASCADE
    )
    league_team = models.ForeignKey(
        League,
        related_name='equipos_league',
        blank=True, null=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
    def __str__(self):
        return self.name.title()

