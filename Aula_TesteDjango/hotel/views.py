from django.shortcuts import render, HttpResponse
from .models import hotel
from .models import quarto
from .forms import FormNome


# Create your views here.

def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context['dados_hotel'] = dados_hotel
    return render(request, 'homepage.html', context)

def quartos(request):
    context = {}
    dados_quartos = quarto.objects.all()
    context["dados_quartos"] = dados_quartos
    return render(request, "quartos.html", context)

def nome(request):
    return render(request, 'nome.html')