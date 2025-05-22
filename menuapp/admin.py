from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    # В данной строке предполагается, что модель MenuItem имеет поля:
    # title, url, is_named, parent, order.
    fields = ('title', 'url', 'is_named', 'parent', 'order')
    autocomplete_fields = ('parent',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # Используется существующее поле 'name' вместо 'title'
    list_display = ('name',)
    # Добавлено, чтобы поддерживать autocomplete_fields в MenuItemAdmin
    search_fields = ('name',)
    inlines = [MenuItemInline]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'order')
    list_filter = ('menu',)
    search_fields = ('title', 'url')  # Предполагаем, что эти поля есть в модели
    ordering = ('menu', 'parent__id', 'order')
    autocomplete_fields = ('menu', 'parent')
