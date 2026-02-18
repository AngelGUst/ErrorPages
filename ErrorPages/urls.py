from django.urls import path
from ErrorPages import views
from core import views as core_views

def trigger_error(request):
    raise Exception("Error intencioal para Error 500.")

urlpatterns = [
    path('', core_views.index, name='index'),
    path('onepage/', core_views.onepage, name='onepage'),
    path('cv/', core_views.cv, name='cv'),
    path('error/', trigger_error),  # This path is just for testing error pages
    path('formulario/', core_views.contacto_view, name="formulario")
]

# Handlers de error
handler500 = views.error_500
handler404 = views.error_404
