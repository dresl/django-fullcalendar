from django.contrib import admin
from .models import CalendarEvent


class CalendarEventAdmin(admin.ModelAdmin):
    model = CalendarEvent
    list_display = ['title', 'constant_cooperation', 'ongoing']
    list_filter = ['start', 'constant_cooperation', 'ongoing']
    search_fields = ['title']


admin.site.register(CalendarEvent, CalendarEventAdmin)
