from django.forms import *
from request.models import *


class RequestForm(ModelForm):
    class Meta:
        model = TravelRequest
        labels = {
            'employee_name': 'Mitarbeiter',
            'destination': 'Reiseziel',
            'event': 'Veranstaltung',
            'cost_center': 'Kostenstelle',
            'journey_start': 'Reisebeginn',
            'journey_end': 'Reiseende',
            'event_start': 'Dienstbeginn',
            'event_end': 'Dienstende'
        }
        exclude = ['status']
        widgets = {
            'employee_name': TextInput(attrs={'readonly': 'readonly'}),
        }

class InvoiceForm(ModelForm):
    class Meta:
        model = TravelInvoice
        labels = {
            'hotel_costs': 'Übernachtungskosten',
            'transport_costs': 'Transportkosten',
            'other_costs': 'Andere Kosten',
            'upload': 'Belege hochladen',
        }
        exclude = ['status']
        widgets = {
            'destination': TextInput(attrs={'readonly': 'readonly'}),
            'event': TextInput(attrs={'readonly': 'readonly'})
        }
