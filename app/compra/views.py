from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.db import transaction

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from app.compra.form import compraForm
from app.compra.models import *
from django.http import JsonResponse, HttpResponse

from app.inventario.models import inventario
from app.mixin import usuariomixin

import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.

class compra_list(LoginRequiredMixin, usuariomixin, ListView):
    model = compra
    template_name = 'compra/compra_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdetalle':
                data = []
                for i in compra.objects.all():
                    data.append(i.toJSON())
            elif action == 'detalle':
                data= []
                for i in detalle_compra.objects.filter(compra_id=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            print(e)
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Compras'
        context['nuevo'] = reverse_lazy('compra:crear')
        context['url'] = reverse_lazy('compra:lista')
        context['entidad'] = 'Compra'
        return context

class compra_create(LoginRequiredMixin, usuariomixin, CreateView):
    model = compra
    form_class = compraForm
    template_name = 'compra/compra_crear.html'
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
                prods = producto.objects.filter(nombre__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    compras = json.loads(request.POST['compra'])
                    c = compra()
                    c.fecha_compra = compras['fecha_compra']
                    c.proveedor_id = compras['proveedor']
                    c.subtotal = float(compras['subtotal'])
                    c.iva = float(compras['iva'])
                    c.total = float(compras['total'])
                    # c.estado =
                    c.save()
                    for i in compras['producto']:
                        det = detalle_compra()
                        det.compra_id = c.id
                        det.producto_id = i['id']
                        det.cantidad = int(i['cantidad'])
                        p = producto.objects.get(pk=i['id'])
                        det.p_compra_actual = p.pvp
                        p.stock = p.stock + int(i['cantidad'])
                        p.save()
                        det.save()
                        for a in range(0, i['cantidad']):
                            inv = inventario()
                            inv.compra_id = c.id
                            inv.producto_id = int(i['id'])
                            inv.save()

            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de Compra'
        context['url'] = reverse_lazy('compra:lista')
        context['entidad'] = 'Compra'
        context['action'] = 'add'
        return context

class pdfcompra(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hola')
