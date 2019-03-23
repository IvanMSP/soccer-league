from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'league_team', 'stadium_team')

admin.site.register(Team, TeamAdmin)
