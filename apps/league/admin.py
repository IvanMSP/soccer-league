from django.contrib import admin
from .models import (
    League,
    Directive,
    Rules,
    Stadium,
)

# Register your models here.
admin.site.register(League)
admin.site.register(Directive)
admin.site.register(Rules)
admin.site.register(Stadium)