from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from error_reports.forms import ErrorReportForm
from error_reports.models import ErrorReport

# Create your views here.

def reporte_error_view(request):
    if request.method == 'GET':
        form = ErrorReportForm()
        return render(request, 'error_reports/reporte_error.html', {'form': form})
    
    elif request.method == 'POST':
        form = ErrorReportForm(request.POST)
        
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'ok',
                'mensaje': 'registro exitoso'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'mensaje': 'algo salio mal',
                'errors': form.errors
            })


def obtener_reportes_view(request):
    reportes = ErrorReport.objects.all().values(
        'id',
        'titulo',
        'descripcion',
        'tipo_error',
        'url',
        'metodo_http',
        'ip_cliente',
        'fecha_reporte',
        'activo'
    )
    
    reportes_list = list(reportes)
    
    return JsonResponse({
        'status': 'ok',
        'reportes': reportes_list
    }, safe=False)
