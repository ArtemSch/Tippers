from django.contrib import admin

from .models import Tipper


@admin.register(Tipper)
class TipperAdmin(admin.ModelAdmin):
    list_display = ('id', 'board_number', 'model', 'max_load_capacity', 'current_weight',)
    list_filter = ('model',)