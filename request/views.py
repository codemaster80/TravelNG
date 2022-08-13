from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from request.forms import *


# Create your views here.
@login_required
def home(request):
    travel_requests = TravelRequest.objects.all().order_by('journey_start')
    travel_invoices = TravelInvoice.objects.all()

    return render(request, 'request/travelRequestList.html',
                  {'page_title': '', 'travel_requests': travel_requests, 'travel_invoices': travel_invoices})


@login_required
def travel_request_details(request, pk=None):
    if pk is None:
        travel_request = TravelRequest()
        page_title = 'Reiseantrag'
        sub_title = 'Antrag erstellen'
    else:
        travel_request = get_object_or_404(TravelRequest, pk=pk)
        page_title = 'Reiseantrag'
        sub_title = 'Antrag ändern'

    if request.method == 'POST':
        form = RequestForm(request.POST, instance=travel_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Bitte Fehler korrigieren')
    else:
        form = RequestForm(instance=travel_request)

    return render(request, 'request/travelForm.html',
                  {'page_title': page_title, 'sub_title': sub_title, 'form': form})


@login_required
def delete_travel_request(request, item_id):
    travel_request = TravelRequest.objects.get(id=item_id)
    travel_request.delete()
    return HttpResponseRedirect(reverse('home'))


@login_required
def delete_travel_invoice(request, item_id):
    travel_invoice = TravelInvoice.objects.get(id=item_id)
    travel_invoice.delete()
    return HttpResponseRedirect(reverse('home'))


@login_required
def travel_invoice_details(request, pk=None):
    if pk is None:
        travel_invoice = TravelInvoice()
        page_title = 'Reisekostenabrechnung'
        sub_title = 'Antrag erstellen'
    else:
        travel_invoice = get_object_or_404(TravelInvoice, pk=pk)
        page_title = 'Reisekostenabrechnung'
        sub_title = 'Antrag ändern'

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=travel_invoice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Bitte Fehler korrigieren')
    else:
        form = InvoiceForm(instance=travel_invoice)

    return render(request, 'request/travelForm.html',
                  {'page_title': page_title, 'sub_title': sub_title, 'form': form})


@login_required
def travel_auth(request):
    return HttpResponseRedirect(reverse('home'))


@login_required
def travel_invoice(request):
    return HttpResponseRedirect(reverse('home'))


def logout_view(request):
    logout(request)
