from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from app.empleado.form import empleadoForm
from app.empleado.models import empleado
from django.views.generic import *

# Create your views here.
class empleado_list(ListView):
    model = empleado
    template_name = 'empleado/empleado_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Empleado'
        context['nuevo'] = reverse_lazy('empleado:crear')
        context['url'] = reverse_lazy('empleado:lista')
        context['entidad'] = 'Empleado'
        return context


class empleado_create(CreateView):
    model = empleado
    form_class = empleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Empleado'
        context['url'] = reverse_lazy('empleado:lista')
        context['entidad'] = 'Empleado'
        return context


class empleado_update(UpdateView):
    model = empleado
    form_class = empleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Empleado'
        context['url'] = reverse_lazy('empleado:lista')
        context['entidad'] = 'Empleado'
        return context


class empleado_delete(DeleteView):
    model = empleado
    form_class = empleadoForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('empleado:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Empleado'
        context['entidad'] = 'Empleado'
        context['url'] = reverse_lazy('empleado:lista')

        return context
