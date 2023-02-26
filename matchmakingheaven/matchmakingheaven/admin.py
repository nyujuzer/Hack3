from django.contrib import admin
from .models import Tournament
from .models import match

admin.site.register(Tournament)
admin.site.register(match)
