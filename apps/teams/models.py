from django.db import models
from league.models import League, Stadium


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    fb_id = models.CharField(max_length=50, blank=True, null=True)
    stadium_team = models.ForeignKey(Stadium, blank=True, null=True, on_delete=models.CASCADE)
    league_team = models.ForeignKey(League, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
    def __str__(self):
        return self.name.title()
    
    def get_players(self):
        return self.team_p.filter(
            id__in=self.player_team.id
        )
