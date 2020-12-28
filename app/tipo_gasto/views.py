from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from app.tipo_gasto.form import tipo_gastoForm
from app.tipo_gasto.models import tipo_gasto
from django.views.generic import *

# Create your views here.
class tgasto_list(ListView):
    model = tipo_gasto
    template_name = 'marca/marca_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tipo de Gastos'
        context['nuevo'] = reverse_lazy('tipo_gasto:crear')
        context['url'] = reverse_lazy('tipo_gasto:lista')
        context['entidad'] = 'Marcas'
        return context


class tgasto_create(CreateView):
    model = tipo_gasto
    form_class = tipo_gastoForm
    template_name = 'tipo_gasto/tipo_gasto_form.html'
    success_url = reverse_lazy('tipo_gasto:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Marca'
        context['url'] = reverse_lazy('tipo_gasto:lista')
        context['entidad'] = 'Marca'
        return context


class tgasto_update(UpdateView):
    model = tipo_gasto
    form_class = tipo_gastoForm
    template_name = 'tipo_gasto/tipo_gasto_form.html'
    success_url = reverse_lazy('tipo_gasto:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Marca'
        context['url'] = reverse_lazy('tipo_gasto:lista')
        context['entidad'] = 'Marca'
        return context

class tgasto_delete(DeleteView):
    model = tipo_gasto
    form_class = tipo_gastoForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('tipo_gasto:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Marca'
        context['entidad'] = 'Marca'
        context['url'] = reverse_lazy('tipo_gasto:lista')

        return context
