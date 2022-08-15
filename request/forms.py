from django.forms import *
from request.models import *


class RequestForm(ModelForm):
    class Meta:
        model = TravelRequest
        labels = {
            'employee': 'Mitarbeiter',
            'destination': 'Reiseziel',
            'event': 'Veranstaltung',
            'cost_center': 'Kostenstelle',
            'journey_start': 'Reisebeginn',
            'journey_end': 'Reiseende',
            'event_start': 'Dienstbeginn',
            'event_end': 'Dienstende'
        }
        exclude = ['username', 'status']
        widgets = {
            'employee': TextInput(attrs={'readonly': 'readonly'})
        }


class InvoiceForm(ModelForm):
    class Meta:
        model = TravelInvoice
        labels = {
            'employee': 'Mitarbeiter',
            'travel_request_id': 'Reiseantrag',
            'hotel_costs': 'Übernachtungskosten',
            'transport_costs': 'Transportkosten',
            'other_costs': 'Andere Kosten',
            'upload': 'Belege hochladen',
        }
        exclude = ['username', 'status']
        widgets = {
            'destination': TextInput(attrs={'readonly': 'readonly', 'placeholder': 'wird automatisch ausgefüllt'}),
            'event': TextInput(attrs={'readonly': 'readonly', 'placeholder': 'wird automatisch ausgefüllt'}),
            'employee': TextInput(attrs={'readonly': 'readonly'})
        }


class AuthForm(ModelForm):
    class Meta:
        model = TravelRequest
        labels = {
            'employee': 'Mitarbeiter',
            'destination': 'Reiseziel',
            'event': 'Veranstaltung',
            'cost_center': 'Kostenstelle',
            'journey_start': 'Reisebeginn',
            'journey_end': 'Reiseende',
            'event_start': 'Dienstbeginn',
            'event_end': 'Dienstende'
        }
        exclude = ['username']
        widgets = {
            'employee': TextInput(attrs={'readonly': 'readonly'}),
            'destination': TextInput(attrs={'readonly': 'readonly'}),
            'event': TextInput(attrs={'readonly': 'readonly'}),
            'cost_center': TextInput(attrs={'readonly': 'readonly'}),
            'journey_start': TextInput(attrs={'readonly': 'readonly'}),
            'journey_end': TextInput(attrs={'readonly': 'readonly'}),
            'event_start': TextInput(attrs={'readonly': 'readonly'}),
            'event_end': TextInput(attrs={'readonly': 'readonly'}),
            'transport': TextInput(attrs={'readonly': 'readonly'})
        }
