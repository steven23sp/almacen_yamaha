from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from app.devolucion.models import devolucion
from app.mixin import usuariomixin
from app.venta.models import venta, detalle_venta


class devolucion_list(LoginRequiredMixin, usuariomixin, ListView):
    model = devolucion
    template_name = 'devoluciones/devoluciones_list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return devolucion.objects.none()

    # def post(self, request, *args, **kwargs):
    #    data = {}
    #    try:
    #        action = request.POST['action']
    #        if action == 'searchdevolucion':
    #            data = []
    #            for i in self.model.objects.all():
    #                data.append(i.toJSON())
    #        elif action == 'report':
    #            data = []
    #           start_date = request.POST.get('start_date', '')
    #            end_date = request.POST.get('end_date', '')
    #            venta = ''
    #            estado = ''
    #            if start_date == '' and end_date == '':
    #               devolucion = self.model.objects.all()
    #           else:
    #                devolucion = self.model.objects.filter(fecha__range=[start_date, end_date])
    #            for c in devolucion:
    #                data.append([
    #                    c.id,
    #                    c.fecha,
    #                    c.venta.fecha_venta,
    #                    c.venta.cliente.nombres,
    #                    c.venta.id,
    #                    format(c.venta.total, '.2f'),
    #                    c.id
    #                ])
    #        else:
    #            data['error'] = 'No ha seleccionado una opcion'
    #    except Exception as e:
    #        data['error'] = str(e)
    #    return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdetalle':
                data = []
                for i in self.model.objects.all():
                    data.append(i.toJSON())
            elif action == 'detalle':
                data = []
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
        context['title'] = 'Listado de Devoluciones'
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Devoluciones'
        return context


class report(LoginRequiredMixin, usuariomixin, ListView):
    model = devolucion
    template_name = 'reporte/devoluciones.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        if action == 'report':
            data = []
            start_date = request.POST.get('start_date', '')
            end_date = request.POST.get('end_date', '')
            try:
                if start_date == '' and end_date == '':
                    d = devolucion.objects.all()
                else:
                    d = devolucion.objects.filter(fecha__range=[start_date, end_date])

                print(d)

                for c in d:
                    data.append([
                        c['fecha'],
                        c['venta__fecha_venta'].strftime("%Y/%m/%d"),
                        c['venta__cliente_nombres'],
                        format(c['venta.subtotal'], '.2f'),
                        format(c['venta.total'], '.2f'),
                    ])
            except:
                pass
            return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['entidad'] = 'Devoluciones'
        data['title'] = 'Reporte de Devoluciones'

        return data
