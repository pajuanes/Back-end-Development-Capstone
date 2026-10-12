from django.contrib import admin

# Register your models here.
from .models import Concert

class ConcertAdmin(admin.ModelAdmin):
    admin.site.register(Concert)

