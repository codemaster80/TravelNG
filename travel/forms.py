from django.forms import *

import travel
from travel import config
from travel.models import *


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
            'event_end': 'Dienstende',
            'transport': 'Verkehrsmittel'
        }
        exclude = ['username', 'status']
        widgets = {
            'employee': TextInput(attrs={'readonly': 'readonly'}),
        }


class InvoiceForm(ModelForm):
    print("forms.py: " + travel.config.ti_username)
    travel_request = ModelChoiceField(queryset=TravelRequest.objects.filter(username='Max.Traveller'))

    class Meta:
        model = TravelInvoice
        labels = {
            'employee': 'Mitarbeiter',
            'travel_request': 'Reiseantrag',
            'journey_start': 'Reisebeginn',
            'journey_end': 'Reiseende',
            'event_start': 'Dienstbeginn',
            'event_end': 'Dienstende',
            'hotel_costs': 'Übernachtungskosten',
            'transport_costs': 'Fahrtkosten',
            'other_costs': 'Andere Kosten',
            'ti_status': 'Status',
            'upload': 'Belege hochladen'
        }
        exclude = ['username', 'tr_status']
        widgets = {
            'destination': TextInput(attrs={'readonly': 'readonly', 'placeholder': 'wird automatisch ausgefüllt'}),
            'event': TextInput(attrs={'readonly': 'readonly', 'placeholder': 'wird automatisch ausgefüllt'}),
            'journey_start': TextInput(attrs={'readonly': 'readonly', 'placeholder': 'wird automatisch ausgefüllt'}),
            'journey_end': TextInput(attrs={'readonly': 'readonly', 'placeholder': 'wird automatisch ausgefüllt'}),
            'event_start': TextInput(attrs={'readonly': 'readonly', 'placeholder': 'wird automatisch ausgefüllt'}),
            'event_end': TextInput(attrs={'readonly': 'readonly', 'placeholder': 'wird automatisch ausgefüllt'}),
            'employee': TextInput(attrs={'readonly': 'readonly'}),
            'ti_status': TextInput(attrs={'readonly': 'readonly'})
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
            'event_end': 'Dienstende',
            'transport': 'Verkehrsmittel'
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


class RefundForm(ModelForm):
    class Meta:
        model = TravelInvoice
        labels = {
            'employee': 'Mitarbeiter',
            'travel_request': 'Reiseantrag',
            'hotel_costs': 'Übernachtungskosten',
            'transport_costs': 'Fahrtkosten',
            'other_costs': 'Andere Kosten',
            'upload': 'Belege hochladen',
            'tr_status': 'Status Reiseantrag',
            'ti_status': 'Status Kostenerstattung'
        }
        exclude = ['username']
        widgets = {
            'destination': TextInput(attrs={'readonly': 'readonly'}),
            'event': TextInput(attrs={'readonly': 'readonly'}),
            'employee': TextInput(attrs={'readonly': 'readonly'}),
            'journey_start': TextInput(attrs={'readonly': 'readonly'}),
            'journey_end': TextInput(attrs={'readonly': 'readonly'}),
            'event_start': TextInput(attrs={'readonly': 'readonly'}),
            'event_end': TextInput(attrs={'readonly': 'readonly'}),
            'hotel_costs': TextInput(attrs={'readonly': 'readonly'}),
            'transport_costs': TextInput(attrs={'readonly': 'readonly'}),
            'other_costs': TextInput(attrs={'readonly': 'readonly'}),
            # 'upload': TextInput(attrs={'readonly': 'readonly'}),
            'tr_status': TextInput(attrs={'readonly': 'readonly'})
        }