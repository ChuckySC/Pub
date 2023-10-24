from django.contrib import admin

from client.models import *

class MenuSectionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    search_fields = ['name', 'type']
    list_filter = [('type')]

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    search_fields = ['name']
    list_filter = [('type')]
    
class EventsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date']
    search_fields = ['name', 'date']
    list_filter = [('date')]

admin.site.register(MenuItems, MenuItemsAdmin)
admin.site.register(Events, EventsAdmin)

# CODEBOOKS / PROPERTIES
admin.site.register(Units)
admin.site.register(MenuSections, MenuSectionsAdmin)