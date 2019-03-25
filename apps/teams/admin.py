from django.contrib import admin
from .models import Team, Category


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'league_team', 'stadium_team', 'category_team')
    list_filter = ('category_team',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Category)
