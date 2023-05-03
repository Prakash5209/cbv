from django.contrib import admin

from detail.models import Books


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',), }