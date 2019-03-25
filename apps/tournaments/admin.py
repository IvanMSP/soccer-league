from django.contrib import admin
from .models import *

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)



