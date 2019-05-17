from django.db import models
from league.models import Team, Category


class Tournament(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    teams = models.ManyToManyField(
        Team,
        related_name='teams',
    )
    category = models.ForeignKey(
        Category, 
        related_name='categorias', 
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Torneo'
        verbose_name_plural = 'Torneos'
    
    def __str__(self):
        return self.name.title()
