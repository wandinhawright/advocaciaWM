from django.contrib import admin
from .models import LeadConsultoria

@admin.register(LeadConsultoria)
class LeadConsultoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'Data_de_Nascimento', 'telefone', 'motivo', 'data_envio')
    list_filter = ('data_envio',)
    search_fields = ('nome', 'email', 'Data_de_Nascimento', 'telefone')
    ordering = ('-data_envio',)
