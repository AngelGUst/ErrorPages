from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        """Procesa todas las excepciones y muestra la página 500"""
        logger.exception(f"Error en {request.path}: {str(exception)}")
        return render(request, '500.html', status=500)