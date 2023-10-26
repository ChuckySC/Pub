from django.contrib import admin

from client.models import *

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1
    show_change_link = True

class MenuSectionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'rid', 'rud']
    search_fields = ['name', 'type']
    list_filter = [('type')]

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'rid', 'rud']
    search_fields = ['name']
    list_filter = [('type')]
    
class EventsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date', 'rid', 'rud']
    search_fields = ['name', 'date']
    list_filter = [('date')]
    
    inlines = [GalleryInline]

admin.site.register(MenuItems, MenuItemsAdmin)
admin.site.register(Events, EventsAdmin)

# CODEBOOKS / PROPERTIES
admin.site.register(Units)
admin.site.register(MenuSections, MenuSectionsAdmin)