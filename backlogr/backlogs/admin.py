from django.contrib import admin

# Register your models here.
from models import Backlog

class BacklogAdmin(admin.ModelAdmin):
    fields = ['uuid']
admin.site.register(Backlog, BacklogAdmin)
