from django.contrib import admin

from Listview.models import ListModel

@admin.register(ListModel)
class ListModelAdmin(admin.ModelAdmin):
    list_display = ("name","description")