from django.shortcuts import render
from app.empresa.form import empresaForm
from app.empresa.models import empresa
from django.views.generic import *
from django.urls import reverse_lazy

class empresa_create(CreateView):
    model = empresa
    form_class = empresaForm
    template_name = 'empresa/empresa_form.html'
    success_url = reverse_lazy('cliente:lista')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Configuracion de la Empresa'
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        return context
