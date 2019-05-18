#Django Core
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#models
from .models import *


class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields':(
                'is_admin_league', 
                'is_admin_team', 
                'is_user_app',
            )
        }),
    )

admin.site.register(User, MyUserAdmin)
admin.site.register(AdminLeagueProfile)
admin.site.register(AdminTeamProfile)
