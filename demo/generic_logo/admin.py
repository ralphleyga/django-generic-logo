from django.contrib import admin

from models import *

class GlogoAdmin(admin.ModelAdmin):
    list_display = ('image', 'user', 'content_type', 'object_id', 'date_added', 'is_primary')

admin.site.register(Glogo, GlogoAdmin)
