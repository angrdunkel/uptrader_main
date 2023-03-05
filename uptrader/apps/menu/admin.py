from django.contrib import admin

from .models import Menu, MenuItem

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'position', 'active', 'created_at'
    )
    list_display_links = ('active', 'created_at',)
    search_fields = (
        'name',
    )
