from django.contrib import admin
from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'url']
    search_fields = ['site_name']


admin.site.register(Bookmark, BookmarkAdmin)
