from django.contrib import admin
from .models import LeadConsultoria

@admin.register(LeadConsultoria)
class LeadConsultoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'motivo', 'data_envio')
    list_filter = ('data_envio',)
    search_fields = ('nome', 'email', 'telefone')
    ordering = ('-data_envio',)
