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

admin.site.register(MenuItems, MenuItemsAdmin)

# CODEBOOKS / PROPERTIES
admin.site.register(Units)
admin.site.register(MenuSections, MenuSectionsAdmin)