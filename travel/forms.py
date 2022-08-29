from django.forms import *
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
    # travel_request = ModelChoiceField(queryset=TravelRequest.objects.filter(username='Max.Traveller'))

    # def __init__(self, *args, **kwargs):
    #     super(InvoiceForm, self).__init__(*args, **kwargs)
    #     if 'user' in kwargs:
    #         user = kwargs.pop('user')
    #         user = 'Max.Traveller'
    #         query = TravelRequest.objects.filter(username=user)
    #         self.fields['travel_request'] = ModelChoiceField(queryset=query, label='Reiseantrag')

    class Meta:
        model = TravelInvoice
        labels = {
            'employee': 'Mitarbeiter',
            'journey_start': 'Reisebeginn',
            'journey_end': 'Reiseende',
            'event_start': 'Dienstbeginn',
            'event_end': 'Dienstende',
            'hotel_costs': 'Übernachtungskosten',
            'transport_costs': 'Fahrtkosten',
            'other_costs': 'Andere Kosten',
            'tr_status': 'Reiseantrag Status',
            'upload': 'Belege hochladen'
        }
        exclude = ['username', 'ti_status']
        widgets = {
            'destination': TextInput(attrs={'readonly': 'readonly'}),
            'event': TextInput(attrs={'readonly': 'readonly'}),
            'journey_start': DateTimeInput(attrs={'readonly': 'readonly'}),
            'journey_end': DateTimeInput(attrs={'readonly': 'readonly'}),
            'event_start': DateTimeInput(attrs={'readonly': 'readonly'}),
            'event_end': DateTimeInput(attrs={'readonly': 'readonly'}),
            'employee': TextInput(attrs={'readonly': 'readonly'}),
            'tr_status': TextInput(attrs={'readonly': 'readonly'})
        }

    def clean(self):
        super(InvoiceForm, self).clean()
        tr_status = self.cleaned_data.get('tr_status')
        if tr_status != 'Genehmigt':
            self.errors['tr_status'] = self.error_class(['Reiseantrag ist nicht genehmigt!'])

        return self.cleaned_data


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
            'cost_center': Select(attrs={'readonly': 'readonly'}),
            'journey_start': DateTimeInput(attrs={'readonly': 'readonly'}),
            'journey_end': DateTimeInput(attrs={'readonly': 'readonly'}),
            'event_start': DateTimeInput(attrs={'readonly': 'readonly'}),
            'event_end': DateTimeInput(attrs={'readonly': 'readonly'}),
            'transport': Select(attrs={'readonly': 'readonly'})
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
            'journey_start': DateTimeInput(attrs={'readonly': 'readonly'}),
            'journey_end': DateTimeInput(attrs={'readonly': 'readonly'}),
            'event_start': DateTimeInput(attrs={'readonly': 'readonly'}),
            'event_end': DateTimeInput(attrs={'readonly': 'readonly'}),
            'hotel_costs': TextInput(attrs={'readonly': 'readonly'}),
            'transport_costs': TextInput(attrs={'readonly': 'readonly'}),
            'other_costs': TextInput(attrs={'readonly': 'readonly'}),
            # 'upload': TextInput(attrs={'readonly': 'readonly'}),
            'tr_status': TextInput(attrs={'readonly': 'readonly'})
        }
