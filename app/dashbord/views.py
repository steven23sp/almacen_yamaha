from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from datetime import datetime
from app.venta.models import *
from app.compra.models import *

# Create your views here.

class dashbord(TemplateView):
    template_name = 'dashbord.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'grafico_ventas_year_month':
                data = self.get_grafico_ventas_year_month()
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

    ################ grafico de ventas  ############################################
    def get_grafico_ventas_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = venta.objects.filter(fecha_venta__year=year, fecha_venta__month=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                data.append(float(total))
        except:
            pass
        return data

    ################ grafico de compras  ############################################
    def get_grafico_compras_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = compra.objects.filter(fecha_compra__year=year, fecha_compra__month=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                data.append(float(total))
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel Administrativo'
        context['title'] = 'Panel Administrativo'
        context['grafico_ventas_year_month'] = self.get_grafico_ventas_year_month()
        context['grafico_compras_year_month'] = self.get_grafico_compras_year_month()
        return context