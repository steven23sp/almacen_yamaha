import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from app.empresa.models import empresa
from app.inventario.models import inventario

from app.venta.form import ventaForm
from app.venta.models import *
from django.http import JsonResponse
from app.mixin import usuariomixin


# Create your views here.

class venta_list(LoginRequiredMixin, usuariomixin, ListView):
    model = venta
    template_name = 'venta/venta_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdetalle':
                data = []
                for i in venta.objects.all():
                    data.append(i.toJSON())
            elif action == 'detalle':
                data= []
                for i in detalle_venta.objects.filter(venta_id=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            print(e)
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ventas'
        context['nuevo'] = reverse_lazy('venta:crear')
        context['url'] = reverse_lazy('venta:lista')
        context['entidad'] = 'Venta'
        return context

class venta_create(LoginRequiredMixin, usuariomixin, CreateView):
    model = venta
    form_class = ventaForm
    template_name = 'venta/venta_crear.html'
    success_url = reverse_lazy('index')

    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = producto.objects.filter(nombre__icontains=request.POST['term'], stock__gte=1)
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            elif action == 'add':
                get = empresa.objects.first()
                ind = 1+(get.indice/100)

                with transaction.atomic():
                    ventas = json.loads(request.POST['venta'])
                    c = venta()
                    c.fecha_venta = ventas['fecha_venta']
                    c.cliente_id = int(ventas['cliente'])
                    c.subtotal = float(ventas['subtotal'])
                    c.iva = float(ventas['iva'])
                    c.total = float(ventas['total'])
                    # c.estado =
                    c.save()
                    for i in ventas['producto']:
                        det = detalle_venta()
                        det.venta_id = c.id
                        det.producto_id = i['id']
                        det.cantidad = int(i['cantidad'])
                        det.subtotal = float(i['subtotal'])
                        p = producto.objects.get(pk=i['id'])
                        det.p_venta_actual = float(i['pvp'])
                        p.stock = p.stock - int(i['cantidad'])
                        p.save()
                        det.save()
                        inv = inventario.objects.filter(producto_id=int(i['id']), estado=1)
                        for it in inv:
                            x = inventario.objects.get(pk=it.id)
                            x.estado = 0
                            x.venta_id = c.id
                            x.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:

            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de Venta'
        context['url'] = reverse_lazy('venta:lista')
        context['entidad'] = 'Venta'
        context['action'] = 'add'
        context['empresa'] = empresa.objects.first()
        return context
