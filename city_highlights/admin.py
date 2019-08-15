from django.contrib import admin

from .models import Highlight


class HighlightAdmin(admin.ModelAdmin):
    # Tuple
    list_display = ('title', 'list_date', 'is_published')


admin.site.register(Highlight, HighlightAdmin)
