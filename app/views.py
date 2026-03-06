from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import ConsultoriaForm


class IndexView(View):
    def get(self, request):
        form = ConsultoriaForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = ConsultoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados enviados com sucesso!')
            return redirect('index')
        return render(request, 'index.html', {'form': form})