from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app.gasto.form import gastoForm
from app.gasto.models import gasto
from django.views.generic import *

# Create your views here.
from app.mixin import usuariomixin


class gasto_list(LoginRequiredMixin,usuariomixin,ListView):
    model = gasto
    template_name = 'gasto/gasto_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in gasto.objects.all():
                    data.append(i.toJSON())
            elif action == 'delete':
                pk = request.POST['id']
                cli = gasto.objects.get(pk=pk)
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
        context['title'] = 'Listado de Gasto'
        context['nuevo'] = reverse_lazy('gasto:crear')
        context['url'] = reverse_lazy('gasto:lista')
        context['entidad'] = 'Gastos'
        return context


class gasto_create(LoginRequiredMixin,usuariomixin,CreateView):
    model = gasto
    form_class = gastoForm
    template_name = 'gasto/gasto_form.html'
    success_url = reverse_lazy('gasto:lista')

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
        context['title'] = 'Registro de Gasto'
        context['url'] = reverse_lazy('gasto:lista')
        context['entidad'] = 'Gasto'
        context['action'] = 'add'
        return context


class gasto_update(LoginRequiredMixin,usuariomixin,UpdateView):
    model = gasto
    form_class = gastoForm
    template_name = 'gasto/gasto_form.html'
    success_url = reverse_lazy('gasto:lista')

   # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            pk = self.kwargs['pk']
            pr = gasto.objects.get(pk=pk)
            if action == 'edit':
                form = self.form_class(request.POST or None, instance=pr)
                data = form.save()
                return HttpResponseRedirect(self.success_url)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de gasto'
        context['url'] = reverse_lazy('gasto:lista')
        context['entidad'] = 'Gasto'
        context['action'] = 'edit'
        return context


#class empleado_delete(LoginRequiredMixin,usuariomixin,DeleteView):
#    model = empleado
#    form_class = empleadoForm
#    template_name = 'form_delete.html'
#    success_url = reverse_lazy('empleado:lista')

    #@method_decorator(login_required)
#    def dispatch(self, request, *args, **kwargs):
#        return super().dispatch(request, *args, **kwargs)

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['title'] = 'Eliminacion de Empleado'
#        context['entidad'] = 'Empleado'
#        context['url'] = reverse_lazy('empleado:lista')

#       return context
