from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date',)
    search_fields = ('name',)

admin.site.register(Event, EventAdmin)