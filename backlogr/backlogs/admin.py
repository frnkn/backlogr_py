from django.contrib import admin

# Register your models here.
from models import Backlog

class BacklogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Backlog, BacklogAdmin)
