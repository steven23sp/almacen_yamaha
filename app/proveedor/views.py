from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from app.proveedor.form import proveedorForm
from app.proveedor.models import proveedor
from django.views.generic import *


# Create your views here.
class proveedor_list(ListView):
    model = proveedor
    template_name = 'proveedor/proveedor_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proveedores'
        context['nuevo'] = reverse_lazy('proveedor:crear')
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedores'
        return context


class proveedor_create(CreateView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Proveedores'
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedores'
        return context


class proveedor_update(UpdateView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Proveedores'
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedor'
        return context


class proveedor_delete(DeleteView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('proveedor:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Proveedor'
        context['entidad'] = 'Proveedor'
        context['url'] = reverse_lazy('proveedor:lista')

        return context
