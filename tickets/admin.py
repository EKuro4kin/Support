from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ("question_name",)
    search_fields = ("question_name",)


admin.site.register(Ticket, TicketAdmin)
