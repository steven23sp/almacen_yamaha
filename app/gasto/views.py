from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app.gasto.form import gastoForm
from app.gasto.models import gasto
from django.views.generic import *

# Create your views here.
from app.mixin import usuariomixin
from app.tipo_gasto.form import tipo_gastoForm
from app.tipo_gasto.models import tipo_gasto


class gasto_list(LoginRequiredMixin, usuariomixin, ListView):
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


class gasto_create(LoginRequiredMixin, usuariomixin, CreateView):
    model = gasto
    form_class = gastoForm
    template_name = 'gasto/gasto_form.html'
    success_url = reverse_lazy('gasto:lista')

    @method_decorator(csrf_exempt)
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
            elif action == 'search_tipo_gasto':
                data = []
                term = request.POST['term']
                prov = tipo_gasto.objects.filter(Q(nombre__icontains=term))[0:10]
                for i in prov:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Gasto'
        context['url'] = reverse_lazy('gasto:lista')
        context['entidad'] = 'Gasto'
        context['action'] = 'add'
        context['formtipogasto'] = tipo_gastoForm
        return context


class gasto_update(LoginRequiredMixin, usuariomixin, UpdateView):
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


class report_fijo(LoginRequiredMixin, usuariomixin, ListView):
    model = gasto
    template_name = 'reporte/gastos.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')

                if start_date == '' and end_date == '':
                    query = gasto.objects.all()
                else:
                    query = gasto.objects.filter(fecha__range=[start_date, end_date],
                                                 tipo_gasto__nombre__icontains=('fijo'))

                    for p in query:
                        data.append(p.toJSON())
        except:
            pass
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['entidad'] = 'Gasto'
        data['title'] = 'Reporte de Gastos Fijos'
        return data


class report_variable(LoginRequiredMixin, usuariomixin, ListView):
    model = gasto
    template_name = 'reporte/gastos.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')

                if start_date == '' and end_date == '':
                    query = gasto.objects.all()
                else:
                    query = gasto.objects.filter(fecha__range=[start_date, end_date],
                                                 tipo_gasto__nombre__icontains=('variable'))
                    for p in query:
                        data.append(p.toJSON())
        except:
            pass
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['entidad'] = 'Gasto'
        data['title'] = 'Reporte de Gastos Variables'
        return data



