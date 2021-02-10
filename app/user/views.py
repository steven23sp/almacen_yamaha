from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app.user.form import userForm
from app.user.models import User
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from app.mixin import usuariomixin


class user_list(LoginRequiredMixin, usuariomixin, ListView):
    model = User
    template_name = 'user/user_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            elif action == 'delete':
                pk = request.POST['id']
                cli = User.objects.get(pk=pk)
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
        context['title'] = 'Listado de Usuarios'
        context['nuevo'] = reverse_lazy('user:crear')
        context['url'] = reverse_lazy('user:lista')
        context['entidad'] = 'Usuarios'
        return context


class user_create(LoginRequiredMixin, usuariomixin, CreateView):
    model = User
    form_class = userForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user:lista')

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
        context['title'] = 'Registro de Usuario'
        context['url'] = reverse_lazy('user:lista')
        context['entidad'] = 'User'
        context['action'] = 'add'
        return context


class user_update(LoginRequiredMixin, usuariomixin, UpdateView):
    model = User
    form_class = userForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user:lista')

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
        context['title'] = 'Edicion de Userio'
        context['url'] = reverse_lazy('user:lista')
        context['entidad'] = 'Usuario'
        context['action'] = 'edit'
        return context
