from django.urls import reverse_lazy

from app.marca.form import marcaForm
from app.marca.models import marca
from django.views.generic import *

# Create your views here.
class marca_list(ListView):
    model = marca
    template_name = 'marca/marca_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Marcas'
        context['nuevo'] = reverse_lazy('marca:crear')
        context['url'] = reverse_lazy('marca:lista')
        context['entidad'] = 'Marcas'
        return context


class marca_create(CreateView):
    model = marca
    form_class = marcaForm
    template_name = 'marca/marca_form.html'
    success_url = reverse_lazy('marca:lista')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Marca'
        context['url'] = reverse_lazy('marca:lista')
        context['entidad'] = 'Marca'
        return context


class marca_update(UpdateView):
    model = marca
    form_class = marcaForm
    template_name = 'marca/marca_form.html'
    success_url = reverse_lazy('marca:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Marca'
        context['url'] = reverse_lazy('marca:lista')
        context['entidad'] = 'Marca'
        return context


class marca_delete(DeleteView):
    model = marca
    form_class = marcaForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('marca:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Marca'
        context['entidad'] = 'Marca'
        context['url'] = reverse_lazy('marca:lista')

        return context
