#Django Core
from django.contrib import admin


#Models
from .models import *

#Models League
admin.site.register(League)
admin.site.register(Directive)
admin.site.register(Rules)
admin.site.register(Stadium)
admin.site.register(Referee)


#Models Teams
admin.site.register(Team)
admin.site.register(Player)



