from django.urls import reverse_lazy

from app.cargo.form import cargoForm
from app.cargo.models import cargo
from django.views.generic import *

# Create your views here.
class cargo_list(ListView):
    model = cargo
    template_name = 'cargo/cargo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cargos'
        context['nuevo'] = reverse_lazy('cargo:crear')
        context['url'] = reverse_lazy('cargo:lista')
        context['entidad'] = 'Cargo'
        return context


class cargo_create(CreateView):
    model = cargo
    form_class = cargoForm
    template_name = 'cargo/cargo_form.html'
    success_url = reverse_lazy('cargo:lista')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Cargo'
        context['url'] = reverse_lazy('cargo:lista')
        context['entidad'] = 'Cargo'
        return context


class cargo_update(UpdateView):
    model = cargo
    form_class = cargoForm
    template_name = 'cargo/cargo_form.html'
    success_url = reverse_lazy('cargo:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Cargo'
        context['url'] = reverse_lazy('cargo:lista')
        context['entidad'] = 'Cargo'
        return context


class cargo_delete(DeleteView):
    model = cargo
    form_class = cargoForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('cargo:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Cargo'
        context['entidad'] = 'cargo'
        context['url'] = reverse_lazy('cargo:lista')

        return context
