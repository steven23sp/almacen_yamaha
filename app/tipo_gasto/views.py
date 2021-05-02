from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app.mixin import usuariomixin
from app.tipo_gasto.form import tipo_gastoForm
from app.tipo_gasto.models import tipo_gasto
from django.views.generic import *

# Create your views here.
class tgasto_list(usuariomixin,ListView):
    model = tipo_gasto
    template_name = 'tipo_gasto/tipo_gasto_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in tipo_gasto.objects.all():
                    data.append(i.toJSON())
            elif action == 'delete':
                pk = request.POST['id']
                cli = tipo_gasto.objects.get(pk=pk)
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
        context['title'] = 'Listado de Tipo de Gastos'
        context['nuevo'] = reverse_lazy('tipo_gasto:crear')
        context['url'] = reverse_lazy('tipo_gasto:lista')
        context['entidad'] = 'Tipo de Gasto'
        return context


class tgasto_create(usuariomixin,CreateView):
    model = tipo_gasto
    form_class = tipo_gastoForm
    template_name = 'tipo_gasto/tipo_gasto_form.html'
    success_url = reverse_lazy('tipo_gasto:lista')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                return HttpResponseRedirect(self.success_url)
            elif action == 'add_tipo_gasto':
                form = self.form_class(request.POST)
                if form.is_valid():
                    pr = form.save()
                    data['tipo_gasto'] = pr.toJSON()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro del tipo de gasto'
        context['url'] = reverse_lazy('tipo_gasto:lista')
        context['entidad'] = 'Tipo de Gasto'
        context['action'] = 'add'

        return context


class tgasto_update(LoginRequiredMixin,usuariomixin,UpdateView):
    model = tipo_gasto
    form_class = tipo_gastoForm
    template_name = 'tipo_gasto/tipo_gasto_form.html'
    success_url = reverse_lazy('tipo_gasto:lista')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion del tipo de gasto'
        context['url'] = reverse_lazy('tipo_gasto:lista')
        context['entidad'] = 'Tipo de Gasto'
        return context

