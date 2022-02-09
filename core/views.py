from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponse
from django.template import loader
from .models import Produto


def index(request):
    prod1 = Produto.objects.all()
    context = {
        'produtos': prod1
    }
    return render(request, 'index.html', context)


def exemplo(request):
    return render(request, 'exemplo.html')


def clientes(request):
    return render(request, 'clientes.html')


def produtos(request, pk):
    prod2 = get_object_or_404(Produto, id=pk)
    context = {
        'produtos': prod2
    }
    return render(request, 'produtos.html', context)


def error404(request, ex):
    template = loader.get_template('error404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('error500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)