from django.shortcuts import render, redirect
from .forms import Formulario

def welcome(request):
    return render(request,'boletin1App/index.html', {})

def hacerFormulario(request):
    enviado = None

    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            fechaInicio = form.cleaned_data['fechaInicio']
            fechaFin = form.cleaned_data['fechaFin']

            enviado = True
    else:
        form = Formulario()

    return render(request, 'boletin1App/hacerFormulario.html', {'form': form, 'enviado': enviado})


