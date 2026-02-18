from django.shortcuts import render
from django.http import HttpResponse
from core.alumno import alumno
from core.forms import ContactoForm
from django.shortcuts import render

from django.shortcuts import render
from .forms import ContactoForm

from django.http import JsonResponse
# Create your views here.
def index(request): 
    return render(request, 'core/index.html')

def onepage(request):
    return render(request, 'core/onepage.html')

def cv(request):
    return render(request, 'core/cv.html')

def nuevo(request):
    variable = alumno("Angel", "Gonzalez", 19)
    return render(request, 'core/nuevo.html', {"alumno": variable})

def contacto_view(request):
    if request.method == 'POST':
        print("se envio un formulario")
    form = ContactoForm()
    return render(request, 'core/formulario.html', {'form': form})


# def contacto_view(request):
#     if request.method == 'POST':
#         form = ContactoForm(request.POST)
#         if form.is_valid():
#             # Los datos ya pasaron las validaciones de front y back
#             nombre = form.cleaned_data['nombre']
#             email = form.cleaned_data['email']
#             mensaje = form.cleaned_data['mensaje']
            
#             print(f"--- NUEVO MENSAJE ---")
#             print(f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}")
            
#             return render(request, 'core/formulario.html', {'form': form, 'success': True})
#     else:
#         form = ContactoForm()

#     return render(request, 'core/formulario.html', {'form': form})

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Los datos ya pasaron las validaciones de front y back
            form.save()

            return JsonResponse({
                'status':'ok',
                'message':'Mensaje recibido.'
            })

            ##return render(request, 'core/formulario.html', {'form': form, 'success': True})

        else:
            return JsonResponse({
                'status':'error',
                'message':'Datos no válidos.',
                'errors': form.errors
            })
    else:
        form = ContactoForm()
    
    return render(request, 'core/formulario.html', {'form': form})