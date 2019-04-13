from django.db import models
from league.models import Stadium, League
#reusable apps
from reusable.constants import *


class Category(models.Model):
    name = models.CharField(max_length=50, **NULL)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name.title()


class Team(models.Model):
    name = models.CharField(max_length=100, **REQUIRED)
    fb_id = models.CharField(max_length=50, **NULL)
    picture = models.ImageField(
        upload_to='teams/picture/',
        max_length=1000,
        blank=True, 
        null=True
    )
    stadium_team = models.ForeignKey(
        Stadium,
        related_name='equipos_stadium',
        **NULL,
        on_delete=models.CASCADE
    )
    league_team = models.ForeignKey(
        League,
        related_name='equipos_league',
        **NULL,
        on_delete=models.CASCADE
    )
    category_team = models.ForeignKey(
        Category,
        related_name='equipos_categories',
        **NULL,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
    def __str__(self):
        return self.name.title()

