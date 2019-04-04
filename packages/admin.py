from django.contrib import admin

from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = ('destination', 'price', 'list_date', 'is_published')
    list_display_links = ('destination',)
    list_editable = ('is_published',)
    search_fields = ('destination', 'description', 'price')
admin.site.register(Package, PackageAdmin)

