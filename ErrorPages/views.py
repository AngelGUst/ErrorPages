from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def error_500(request):
    """Manejador personalizado para errores 500"""
    try:
        return render(request, '500.html', status=500)
    except Exception as e:
        logger.exception("Error renderizando 500.html")
        # Si la template falla, retorna HTML directo
        return HttpResponse(
            '''<!DOCTYPE html>
            <html><head><meta charset="UTF-8"><title>Error 500</title></head>
            <body style="display:flex;align-items:center;justify-content:center;height:100vh;background:linear-gradient(135deg,#667eea,#764ba2);margin:0">
            <div style="max-width:720px;padding:3rem;background:rgba(255,255,255,0.95);border-radius:12px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.3)">
            <h1 style="color:#d32f2f;font-size:2.5rem">¡Oops! Error 500</h1>
            <p style="color:#666;font-size:1.1rem">Algo salió mal en el servidor. Estamos trabajando para solucionarlo.</p>
            <a href="/" style="display:inline-block;padding:0.75rem 1.5rem;background:#667eea;color:#fff;text-decoration:none;border-radius:6px;font-weight:bold">Volver al inicio</a>
            </div></body></html>''',
            status=500,
            content_type='text/html'
        )

def error_404(request, exception=None):
    """Manejador personalizado para errores 404"""
    try:
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.exception("Error renderizando 404.html")
        # Si la template falla, retorna HTML directo
        return HttpResponse(
            '''<!DOCTYPE html>
            <html><head><meta charset="UTF-8"><title>Error 404</title></head>
            <body style="display:flex;align-items:center;justify-content:center;height:100vh;background:linear-gradient(135deg,#667eea,#764ba2);margin:0">
            <div style="max-width:420px;padding:1.5rem;background:rgba(255,255,255,0.95);border-radius:12px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.3)">
            <h1 style="color:#f5576c;font-size:2rem">¡Oops! Error 404</h1>
            <p style="color:#666;font-size:0.95rem">La página que buscas se ha perdido en el espacio digital.</p>
            <a href="/" style="display:inline-block;padding:0.6rem 1.25rem;background:#f5576c;color:#fff;text-decoration:none;border-radius:6px;font-weight:bold">Ir al inicio</a>
            </div></body></html>''',
            status=404,
            content_type='text/html'
        )