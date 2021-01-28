from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app.mixin import usuariomixin
from app.proveedor.form import proveedorForm
from app.proveedor.models import proveedor
from django.views.generic import *


# Create your views here.
class proveedor_list(LoginRequiredMixin, usuariomixin, ListView):
    model = proveedor
    template_name = 'proveedor/proveedor_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in proveedor.objects.all():
                    data.append(i.toJSON())
            elif action == 'delete':
                pk = request.POST['id']
                cli = proveedor.objects.get(pk=pk)
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
        context['title'] = 'Listado de Proveedores'
        context['nuevo'] = reverse_lazy('proveedor:crear')
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedores'
        return context


class proveedor_create(LoginRequiredMixin, usuariomixin, CreateView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:lista')

    # @method_decorator(login_required)
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
        context['title'] = 'Registro de Proveedores'
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedores'
        context['action'] = 'add'
        return context


class proveedor_update(LoginRequiredMixin, usuariomixin, UpdateView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:lista')

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
        context['title'] = 'Edicion de Proveedores'
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedor'
        context['action'] = 'edit'
        return context


class proveedor_delete(LoginRequiredMixin, usuariomixin, DeleteView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('proveedor:lista')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
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
        context['title'] = 'Eliminacion de Proveedor'
        context['entidad'] = 'Proveedor'
        context['url'] = reverse_lazy('proveedor:lista')

        return context
