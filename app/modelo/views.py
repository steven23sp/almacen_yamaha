from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from app.modelo.form import modeloForm
from app.modelo.models import modelo
from django.views.generic import *

# Create your views here.
class modelo_list(ListView):
    model = modelo
    template_name = 'cargo/cargo_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Modelos'
        context['nuevo'] = reverse_lazy('modelo:crear')
        context['url'] = reverse_lazy('modelo:lista')
        context['entidad'] = 'Modelos'
        return context


class modelo_create(CreateView):
    model = modelo
    form_class = modeloForm
    template_name = 'modelo/modelo_form.html'
    success_url = reverse_lazy('modelo:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Modelo'
        context['url'] = reverse_lazy('modelo:lista')
        context['entidad'] = 'Modelo'
        return context


class modelo_update(UpdateView):
    model = modelo
    form_class = modeloForm
    template_name = 'modelo/modelo_form.html'
    success_url = reverse_lazy('modelo:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Modelo'
        context['url'] = reverse_lazy('modelo:lista')
        context['entidad'] = 'Modelo'
        return context


class modelo_delete(DeleteView):
    model = modelo
    form_class = modeloForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('modelo:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Modelo'
        context['entidad'] = 'Modelo'
        context['url'] = reverse_lazy('modelo:lista')

        return context
