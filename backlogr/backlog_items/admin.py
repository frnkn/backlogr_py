from django.contrib import admin

# Register your models here.

# Register your models here.
from models import BacklogItem

class BacklogItemAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'user', 'backlog', 'backlog_item_type', 'list_ui_rank', 'parent_uuid', 'created_on', 'updated_on')
admin.site.register(BacklogItem, BacklogItemAdmin)
