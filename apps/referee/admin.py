from django.contrib import admin
from .models import Referee


class RefereeAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'referee_league', 'nationality')
    list_filter = ('referee_league',)
admin.site.register(Referee, RefereeAdmin)
