from django.db import models

class PerfilAdvogado(models.Model):
    nome = models.CharField(max_length=100)
    oab = models.CharField(max_length=20, help_text="Ex: OAB/SP 123.456")
    foto = models.ImageField(upload_to='advogados/')
    biografia_curta = models.TextField(help_text="Aparece no topo (Hero)")
    biografia_completa = models.TextField(help_text="Aparece na seção 'Sobre'")
    anos_experiencia = models.PositiveIntegerField(default=0)
    casos_concluidos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Especialidade(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem de exibição no site")

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo
    
class LeadConsultoria(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.PositiveIntegerField()
    motivo = models.TextField(verbose_name="Motivo da Procura")
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.data_envio.strftime('%d/%m/%Y')}"