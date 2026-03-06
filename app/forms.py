from django import forms
from .models import LeadConsultoria
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ConsultoriaForm(forms.ModelForm):
    class Meta:
        model = LeadConsultoria
        fields = ['nome', 'idade', 'telefone', 'email', 'motivo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # Estilizando o botão para combinar com seu layout dourado
        self.helper.add_input(Submit('submit', 'Enviar Solicitação', css_class='btn-gold w-100'))