from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Participant



@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'participant_type', 'qr_code')
    readonly_fields = ('qr_code', 'qr_preview', 'qr_image')

    def qr_preview(self, obj):
        if obj.qr_image:
           return format_html(
                '<img src="{}" width="150" height="150" />',
                obj.qr_image.url
            )
        return "Sem QR"
    
    qr_preview.short_description = "QR Code"

admin.site.register(Event)    

