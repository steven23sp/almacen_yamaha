from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from app.empresa.form import empresaForm
from app.empresa.models import empresa
from django.views.generic import *

# Create your views here.
class empresa_list(ListView):
    model = empresa
    template_name = 'empresa/empresa_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Empresa'
        #context['nuevo'] = reverse_lazy('cliente:crear')
        #context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Empresa'
        return context

class empresa_update(UpdateView):
    model = empresa
    form_class = empresaForm
    template_name = 'empresa/empresa_form.html'
    success_url = reverse_lazy('empleado:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Empresa'
        context['url'] = reverse_lazy('empresa:lista')
        context['entidad'] = 'Empresa'
        return context


class empresa_delete(DeleteView):
    model = empresa
    form_class = empresaForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('empleado:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Empresa'
        context['entidad'] = 'Empresa'
        context['url'] = reverse_lazy('empresa:lista')

        return context
