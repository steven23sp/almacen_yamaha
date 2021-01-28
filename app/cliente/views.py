from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app.cliente.form import clienteForm
from app.cliente.models import cliente
from django.views.generic import *
from app.mixin import usuariomixin


# from django.http import JsonResponse

# Create your views here.


class cliente_list(LoginRequiredMixin, usuariomixin, ListView):
    model = cliente
    template_name = 'cliente/cliente_list.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in cliente.objects.all():
                    data.append(i.toJSON())
            elif action == 'delete':
                pk = request.POST['id']
                cli = cliente.objects.get(pk=pk)
                cli.delete()
                data['resp'] = True
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            print(e)
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['nuevo'] = reverse_lazy('cliente:crear')
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        return context


class cliente_create(LoginRequiredMixin, usuariomixin, CreateView):
    model = cliente
    form_class = clienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:lista')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
                return HttpResponseRedirect(self.success_url)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Cliente'
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        context['action'] = 'add'
        return context


class cliente_update(LoginRequiredMixin, usuariomixin, UpdateView):
    model = cliente
    form_class = clienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:lista')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
                return HttpResponseRedirect(self.success_url)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Cliente'
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        context['action'] = 'edit'
        return context


class cliente_delete(LoginRequiredMixin, usuariomixin, DeleteView):
    model = cliente
    form_class = clienteForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('cliente:lista')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Cliente'
        context['entidad'] = 'Cliente'
        context['url'] = reverse_lazy('cliente:lista')
        context['action'] = 'delete'

        return context
