from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from request.models import *
from request.forms import *


# Create your views here.
@login_required
def home(request):
    travel_requests = TravelRequest.objects.all().order_by('journey_start')

    return render(request, 'request/travelRequestList.html',
                  {'page_title': '', 'travel_requests': travel_requests})


@login_required
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


@login_required
def delete_travel_request(request, item_id):
    travel_request = TravelRequest.objects.get(id=item_id)
    travel_request.delete()
    return HttpResponseRedirect(reverse('home'))


@login_required
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

    return render(request, 'request/travelInvoice.html', {'page_title': 'Reisekostenabrechnung', 'form': form})


@login_required
def travel_auth(request):
    return HttpResponseRedirect(reverse('home'))


@login_required
def travel_invoice(request):
    return HttpResponseRedirect(reverse('home'))


def logout_view(request):
    logout(request)
