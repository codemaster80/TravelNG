from django.forms import *
from request.models import *


class RequestForm(ModelForm):
    class Meta:
        model = TravelRequest
        labels = {
            'destination': 'Reiseziel',
            'event': 'Veranstaltung',
            'cost_center': 'Kostenstelle',
            'employee': 'Mitarbeiter'
        }
        fields = '__all__'


class InvoiceForm(ModelForm):
    class Meta:
        model = TravelInvoice
        labels = {
            'hotel_costs': 'Übernachtungskosten',
            'transport_costs': 'Transportkosten',
            'other_costs': 'Andere Kosten',
        }
        fields = '__all__'
