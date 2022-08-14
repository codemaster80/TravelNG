import time

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
        tr = TravelRequest()
        tr.username = request.user.get_username()
        tr.employee = request.user.get_full_name()
        page_title = 'Reiseantrag'
        sub_title = 'Antrag erstellen'
    else:
        tr = get_object_or_404(TravelRequest, pk=pk)
        page_title = 'Reiseantrag'
        sub_title = 'Antrag ändern'

    if request.method == 'POST':
        form = RequestForm(request.POST, instance=tr)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Bitte Fehler korrigieren')
    else:
        form = RequestForm(instance=tr)

    return render(request, 'request/travelForm.html',
                  {'page_title': page_title, 'sub_title': sub_title, 'form': form})


@login_required
def delete_travel_request(request, item_id):
    tr = TravelRequest.objects.get(id=item_id)
    tr.delete()
    messages.success(request, 'Gelöscht')
    return HttpResponseRedirect(reverse('home'))


@login_required
def delete_travel_invoice(request, item_id):
    ti = TravelInvoice.objects.get(id=item_id)
    ti.delete()
    messages.success(request, 'Gelöscht')
    return HttpResponseRedirect(reverse('home'))


@login_required
def travel_invoice_details(request, pk=None):
    if pk is None:
        ti = TravelInvoice()
        ti.username = request.user.get_username()
        ti.employee = request.user.get_full_name()
        page_title = 'Reisekostenabrechnung'
        sub_title = 'Antrag erstellen'
    else:
        ti = get_object_or_404(TravelInvoice, pk=pk)
        page_title = 'Reisekostenabrechnung'
        sub_title = 'Antrag ändern'

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=ti)
        if form.is_valid():
            form.save()
            tr_data = TravelRequest.objects.get(id=ti.travel_request_id)
            ti.event = tr_data.event
            ti.destination = tr_data.destination
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Bitte Fehler korrigieren')
    else:
        form = InvoiceForm(instance=ti)

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
