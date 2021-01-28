from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app.cargo.form import cargoForm
from app.cargo.models import cargo
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from app.mixin import usuariomixin


class cargo_list(LoginRequiredMixin, usuariomixin, ListView):
    model = cargo
    template_name = 'cargo/cargo_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in cargo.objects.all():
                    data.append(i.toJSON())
            elif action == 'delete':
                pk = request.POST['id']
                cli = cargo.objects.get(pk=pk)
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
        context['title'] = 'Listado de Cargos'
        context['nuevo'] = reverse_lazy('cargo:crear')
        context['url'] = reverse_lazy('cargo:lista')
        context['entidad'] = 'Cargo'
        return context


class cargo_create(LoginRequiredMixin, usuariomixin, CreateView):
    model = cargo
    form_class = cargoForm
    template_name = 'cargo/cargo_form.html'
    success_url = reverse_lazy('cargo:lista')

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
        context['title'] = 'Registro de Cargo'
        context['url'] = reverse_lazy('cargo:lista')
        context['entidad'] = 'Cargo'
        context['action'] = 'add'
        return context


class cargo_update(LoginRequiredMixin, usuariomixin, UpdateView):
    model = cargo
    form_class = cargoForm
    template_name = 'cargo/cargo_form.html'
    success_url = reverse_lazy('cargo:lista')

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
        context['title'] = 'Edicion de Cargo'
        context['url'] = reverse_lazy('cargo:lista')
        context['entidad'] = 'Cargo'
        context['action'] = 'edit'
        return context


class cargo_delete(LoginRequiredMixin, usuariomixin, DeleteView):
    model = cargo
    form_class = cargoForm
    template_name = 'form_delete.html'
    success_url = reverse_lazy('cargo:lista')

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
        context['title'] = 'Eliminacion de Cargo'
        context['entidad'] = 'cargo'
        context['url'] = reverse_lazy('cargo:lista')

        return context
