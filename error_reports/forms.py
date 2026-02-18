from django import forms
from django.core.exceptions import ValidationError
import re
from error_reports.models import ErrorReport

class ErrorReportForm(forms.ModelForm):

    class Meta:
        model = ErrorReport
        fields = ['titulo', 'descripcion', 'tipo_error', 'url', 'metodo_http', 'ip_cliente']