from django.shortcuts import render


# Create your views here.
def menu(request):
    data = {
        'title': 'Menu Principal', 'entidad': 'Menu Principal'
    }
    return render(request, '../../sistema_yamaha/templates/index.html', data)
    #return render(request, 'bases/base.html', data)