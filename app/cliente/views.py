from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from app.cliente.form import clienteForm
from app.cliente.models import cliente
from django.views.generic import *
#from django.http import JsonResponse

# Create your views here.
class cliente_list(ListView):
    model = cliente
    template_name = 'cliente/cliente_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['nuevo'] = reverse_lazy('cliente:crear')
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        return context

    '''def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'busqueda':
                data = []
                for i in cliente.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) '''

class cliente_create(CreateView):
    model = cliente
    form_class = clienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Cliente'
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        return context


class cliente_update(UpdateView):
    model = cliente
    form_class = clienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Cliente'
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        return context


class cliente_delete(DeleteView):
    model = cliente
    form_class = clienteForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('cliente:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Cliente'
        context['entidad'] = 'Cliente'
        context['url'] = reverse_lazy('cliente:lista')

        return context
