from django.contrib import admin
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'number', 'postion', 'team_player')
    list_filter = ('team_player',)

    def full_name(self, obj):
        return obj.name + ' ' + obj.last_name

admin.site.register(Player, PlayerAdmin)
