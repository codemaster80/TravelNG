import io
import os.path

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

import travel.config
from travel.forms import *


# Create your views here.
@login_required
def home(request):
    if request.user.get_username() == 'admin':
        print('User is admin')
        travel_requests = TravelRequest.objects.all().order_by('journey_start')
        travel_invoices = TravelInvoice.objects.all().order_by('journey_start')
        return render(request, 'travel/home.html',
                      {'page_title': '', 'travel_requests': travel_requests, 'travel_invoices': travel_invoices})
    elif request.user.has_perm('travel.is_supervisor'):
        print('user is supervisor')
        travel_requests = TravelRequest.objects.filter(username=request.user.get_username()).order_by('journey_start')
        travel_invoices = TravelInvoice.objects.filter(username=request.user.get_username()).order_by('journey_start')
        travel_auth = TravelRequest.objects.filter(status='In Bearbeitung').order_by('journey_start')
        return render(request, 'travel/home.html',
                      {'page_title': '', 'travel_requests': travel_requests, 'travel_invoices': travel_invoices,
                       'travel_auth': travel_auth})

    elif request.user.has_perm('travel.is_clerk'):
        print('User is clerk')
        travel_requests = TravelRequest.objects.filter(username=request.user.get_username()).order_by('journey_start')
        travel_invoices = TravelInvoice.objects.filter(username=request.user.get_username()).order_by('journey_start')
        travel_refund = TravelInvoice.objects.filter(tr_status='Genehmigt').filter(ti_status='In Bearbeitung').order_by(
            'journey_start')
        return render(request, 'travel/home.html',
                      {'page_title': '', 'travel_requests': travel_requests, 'travel_invoices': travel_invoices,
                       'travel_refund': travel_refund})
    else:
        print("User is employee")
        travel_requests = TravelRequest.objects.filter(username=request.user.get_username()).order_by('journey_start')
        travel_invoices = TravelInvoice.objects.filter(username=request.user.get_username()).order_by('journey_start')
        return render(request, 'travel/home.html',
                      {'page_title': '', 'travel_requests': travel_requests, 'travel_invoices': travel_invoices})


@login_required
def travel_request_details(request, pk=None):
    # new travel
    if pk is None:
        tr = TravelRequest()
        tr.username = request.user.get_username()
        tr.employee = request.user.get_full_name()
        page_title = 'Reiseantrag'
        sub_title = 'Antrag erstellen'
    # edit travel
    else:
        tr = get_object_or_404(TravelRequest, pk=pk)
        page_title = 'Reiseantrag'
        sub_title = 'Antrag ändern'

    # if submit button pressed
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

    return render(request, 'travel/travelForm.html',
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
    # print(ti.upload.path)
    if ti.upload is None:
        if os.path.exists(ti.upload.path):
            os.remove(ti.upload.path)
    ti.delete()
    messages.success(request, 'Gelöscht')
    return HttpResponseRedirect(reverse('home'))


@login_required
def travel_invoice_details(request, tr_pk=None, ti_pk=None):
    # invoice overview
    if (tr_pk is None) and (ti_pk is None):
        ti = TravelInvoice()
        page_title = 'Reisekostenerstattung'
        sub_title = 'Reiseantrag auswählen'
        travel_requests = TravelRequest.objects.filter(username=request.user.get_username()).order_by(
            'journey_start')

        return render(request, 'travel/travelInvoice.html',
                      {'page_title': page_title, 'sub_title': sub_title, 'travel_requests': travel_requests})
    # add invoice
    elif (tr_pk is not None) and (ti_pk is None):
        page_title = 'Reisekostenerstattung'
        sub_title = 'Antrag erstellen'
        tr = get_object_or_404(TravelRequest, pk=tr_pk)
        ti.username = tr.username
        ti.employee = tr.employee
        ti.event = tr.event
        ti.destination = tr.destination
        ti.journey_start = tr.journey_start
        ti.journey_end = tr.journey_end
        ti.event_start = tr.event_start
        ti.event_end = tr.event_end
        ti.tr_status = tr.status
    # edit invoice
    else:
        page_title = 'Reisekostenerstattung'
        sub_title = 'Antrag ändern'
        ti = get_object_or_404(TravelInvoice, pk=ti_pk)

    # if submit button pressed
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES, instance=ti)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Bitte Fehler korrigieren')
    else:
        form = InvoiceForm(instance=ti)

    return render(request, 'travel/travelForm.html',
                  {'page_title': page_title, 'sub_title': sub_title, 'form': form})


@login_required
def travel_auth_details(request, pk=None):
    page_title = 'Reisegenehmigung'
    sub_title = 'Antrag genehmigen'
    if pk is None:
        travel_requests = TravelRequest.objects.all().order_by('journey_start')
        return render(request, 'travel/travelAuth.html',
                      {'page_title': page_title, 'sub_title': sub_title, 'travel_requests': travel_requests})

    tr = get_object_or_404(TravelRequest, pk=pk)

    if request.method == 'POST':
        form = AuthForm(request.POST, instance=tr)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Bitte Fehler korrigieren')
    else:
        form = AuthForm(instance=tr)

    return render(request, 'travel/travelForm.html',
                  {'page_title': page_title, 'sub_title': sub_title, 'form': form})


@login_required
def travel_invoice_refund(request, pk=None):
    if pk is None:
        travel_invoices = TravelInvoice.objects.filter(tr_status='Genehmigt').filter(
            ti_status='In Bearbeitung').order_by(
            'journey_start')
        return render(request, 'travel/travelRefund.html',
                      {'travel_invoices': travel_invoices})
    else:
        ti = get_object_or_404(TravelInvoice, pk=pk)
        page_title = 'Reisekostenerstattung'
        sub_title = 'Antrag bearbeiten'

    if request.method == 'POST':
        form = RefundForm(request.POST, instance=ti)
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
        form = RefundForm(instance=ti)

    return render(request, 'travel/travelForm.html',
                  {'page_title': page_title, 'sub_title': sub_title, 'form': form})


@login_required
def create_pdf_document(request, pdf=None, pk=None):
    pk = pk
    buffer = io.BytesIO()
    page = canvas.Canvas(buffer, pagesize=A4, bottomup=0)

    # draw page
    text = page.beginText()
    text.setTextOrigin(cm, cm)
    text.setFont("Helvetica", 12, leading=20)

    if pdf == 'tr':
        tr_data = TravelRequest.objects.get(id=pk)
        lines = [
            'Reiseantrag',
            ' ',
            'Mitarbeiter: ' + tr_data.employee,
            'Reiseziel: ' + tr_data.destination,
            'Veranstaltung: ' + tr_data.event,
            'Reisebeginn: ' + str(tr_data.journey_start),
            'Reiseende: ' + str(tr_data.journey_end),
            'Dienstbeginn: ' + str(tr_data.event_start),
            'Dienstende: ' + str(tr_data.event_end),
            'Transportmittel: ' + str(tr_data.transport),
            'Kostenstelle: ' + str(tr_data.cost_center)
        ]
    else:
        ti_data = TravelInvoice.objects.get(id=pk)
        lines = [
            'Reisekostenabrechnung',
            ' ',
            'Mitarbeiter: ' + ti_data.employee,
            'Reiseziel: ' + ti_data.destination,
            'Veranstaltung: ' + ti_data.event,
            'Reisebeginn: ' + str(ti_data.journey_start),
            'Reiseende: ' + str(ti_data.journey_end),
            'Dienstbeginn: ' + str(ti_data.event_start),
            'Dienstende: ' + str(ti_data.event_end),
            'Übernachtungskosten: ' + str(ti_data.hotel_costs),
            'Fahrtkosten: ' + str(ti_data.transport_costs),
            'Nebenkosten: ' + str(ti_data.other_costs),
        ]

    for line in lines:
        text.textLine(line)

    page.drawText(text)
    page.showPage()
    page.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Travel-PDF.pdf')


def logout_view(request):
    logout(request)
