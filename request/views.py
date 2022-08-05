from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from request.models import *
from request.forms import *


# Create your views here.
def home(request):
    return render(request, 'request/base.html', {'page_title': 'Start'})


def new_travel_request(request):
    travel_request = TravelRequest()

    if request.method == 'POST':
        # Formular abgeschickt
        form = RequestForm(request.POST, instance=travel_request)
        if form.is_valid():
            form.save()
            # Pruefung erfolgreich
            return HttpResponseRedirect(reverse('home'))
        else:
            # Pruefung nicht erfolgreich
            pass
    else:
        form = RequestForm(instance=travel_request)

    return render(request, 'request/travelRequest.html', {'page_title': 'Reiseantrag', 'form': form})


def new_travel_invoice(request):
    travel_invoice = TravelInvoice()

    if request.method == 'POST':
        # Formular abgeschickt
        form = RequestForm(request.POST, instance=travel_invoice)
        if form.is_valid():
            form.save()
            # Pruefung erfolgreich
            return HttpResponseRedirect(reverse('home'))
        else:
            # Pruefung nicht erfolgreich
            pass
    else:
        form = InvoiceForm(instance=travel_invoice)

    return render(request, 'request/travelInvoice.html', {'page_title': 'Reiseabrechnung', 'form': form})

