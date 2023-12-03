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

from travel.forms import *


# Create your views here.
@login_required
def startpage(request):
    if request.user.get_username() == 'admin':
        print('User is admin')
        travel_requests = TravelRequest.objects.all().order_by('journey_start')
        travel_invoices = TravelInvoice.objects.all().order_by('journey_start')
        return render(request, 'travel/home.html',
                      {'page_title': '', 'travel_requests': travel_requests, 'travel_invoices': travel_invoices})
    elif request.user.has_perm('travel.is_supervisor'):
        print('user is supervisor')
        travel_invoices, travel_requests = collect_data(request)
        travel_auth = TravelRequest.objects.filter(status='In Bearbeitung',
                                                   supervisor=request.user.get_username()).order_by('journey_start')
        return render(request, 'travel/home.html',
                      {'page_title': '', 'travel_requests': travel_requests, 'travel_invoices': travel_invoices,
                       'travel_auth': travel_auth})
    elif request.user.has_perm('travel.is_clerk'):
        print('User is clerk')
        travel_invoices, travel_requests = collect_data(request)
        travel_refund = TravelInvoice.objects.filter(tr_status='Genehmigt').filter(ti_status='In Bearbeitung').order_by(
            'journey_start')
        return render(request, 'travel/home.html',
                      {'page_title': '', 'travel_requests': travel_requests, 'travel_invoices': travel_invoices,
                       'travel_refund': travel_refund})
    else:
        print("User is employee")
        travel_invoices, travel_requests = collect_data(request)
        return render(request, 'travel/home.html',
                      {'page_title': '', 'travel_requests': travel_requests, 'travel_invoices': travel_invoices})


def collect_data(request):
    travel_requests = TravelRequest.objects.filter(username=request.user.get_username()).order_by('journey_start')
    travel_invoices = TravelInvoice.objects.filter(username=request.user.get_username()).order_by('journey_start')
    return travel_invoices, travel_requests


class FormSubmit:
    @staticmethod
    def submit(form_name, instance_name, request):
        if request.method == 'POST':
            form = form_name(request.POST, instance=travel_request)
            if form.is_valid():
                form.save()
                messages.success(request, 'Gespeichert')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, 'Bitte Fehler korrigieren')
        else:
            form = form_name(instance=instance_name)
        return form


@login_required
def travel_request_details(request, pk=None, delete_id=None):
    # delete travel request
    if delete_id is not None:
        travel_request = TravelRequest.objects.get(id=delete_id)
        travel_request.delete()
        messages.success(request, 'Gelöscht')
        return HttpResponseRedirect(reverse('home'))
    # new travel request
    elif pk is None:
        travel_request = TravelRequest()
        travel_request.username = request.user.get_username()
        travel_request.employee = request.user.get_full_name()
        user = User.objects.get(username=travel_request.username)
        travel_request.supervisor = user.employee.supervisor
        page_title = 'Reiseantrag'
        sub_title = 'Antrag erstellen'
    # edit travel
    else:
        travel_request = get_object_or_404(TravelRequest, pk=pk)
        page_title = 'Reiseantrag'
        sub_title = 'Antrag ändern'
    # if submit button pressed
    form = FormSubmit.submit('RequestForm', 'travel_request', request)
    return render(request, 'travel/travelForm.html',
                  {'page_title': page_title, 'sub_title': sub_title, 'form': form})


@login_required
def travel_invoice_details(request, travel_request_pk=None, travel_invoice_pk=None, delete_id=None):
    # delete travel invoice
    if delete_id is not None:
        travel_invoice = TravelInvoice.objects.get(id=delete_id)
        if travel_invoice.upload is None:
            if os.path.exists(travel_invoice.upload.path):
                os.remove(travel_invoice.upload.path)
        travel_invoice.delete()
        messages.success(request, 'Gelöscht')
        return HttpResponseRedirect(reverse('home'))
    # invoice overview
    elif (travel_request_pk is None) and (travel_invoice_pk is None):
        page_title = 'Reisekostenerstattung'
        sub_title = 'Reiseantrag auswählen'
        travel_requests = TravelRequest.objects.filter(username=request.user.get_username()).order_by(
            'journey_start')
        return render(request, 'travel/travelInvoice.html',
                      {'page_title': page_title, 'sub_title': sub_title, 'travel_requests': travel_requests})
    # add invoice
    elif (travel_request_pk is not None) and (travel_invoice_pk is None):
        page_title = 'Reisekostenerstattung'
        sub_title = 'Antrag erstellen'
        travel_request = get_object_or_404(TravelRequest, pk=travel_request_pk)
        travel_invoice = TravelInvoice()
        travel_invoice.username = travel_request.username
        travel_invoice.employee = travel_request.employee
        travel_invoice.event = travel_request.event
        travel_invoice.destination = travel_request.destination
        travel_invoice.journey_start = travel_request.journey_start
        travel_invoice.journey_end = travel_request.journey_end
        travel_invoice.event_start = travel_request.event_start
        travel_invoice.event_end = travel_request.event_end
        travel_invoice.tr_status = travel_request.status
    # edit invoice
    else:
        page_title = 'Reisekostenerstattung'
        sub_title = 'Antrag ändern'
        travel_invoice = get_object_or_404(TravelInvoice, pk=travel_invoice_pk)
    # if submit button pressed
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES, instance=travel_invoice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Bitte Fehler korrigieren')
    else:
        form = InvoiceForm(instance=travel_invoice)
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
    travel_request = get_object_or_404(TravelRequest, pk=pk)
    form = FormSubmit.submit('AuthForm', 'travel_request', request)
    return render(request, 'travel/travelForm.html',
                  {'page_title': page_title, 'sub_title': sub_title, 'form': form})


@login_required
def travel_invoice_refund(request, pk=None):
    # refund overview
    if pk is None:
        travel_invoices = TravelInvoice.objects.filter(tr_status='Genehmigt').filter(
            ti_status='In Bearbeitung').order_by('journey_start')
        return render(request, 'travel/travelRefund.html',
                      {'travel_invoices': travel_invoices})
    # refund change
    else:
        travel_invoice = get_object_or_404(TravelInvoice, pk=pk)
        page_title = 'Reisekostenerstattung'
        sub_title = 'Antrag bearbeiten'
        form = FormSubmit.submit('RefundForm', 'travel_invoice', request)
    return render(request, 'travel/travelForm.html',
                  {'page_title': page_title, 'sub_title': sub_title, 'form': form})


@login_required
def create_pdf_document(request, pdf=None, pk=None):
    file_buffer = io.BytesIO()
    page = canvas.Canvas(file_buffer, pagesize=A4, bottomup=0)
    # draw page
    text = page.beginText()
    text.setTextOrigin(cm, cm)
    text.setFont("Helvetica", 12, leading=20)
    if pdf == 'tr':
        travel_request_data = TravelRequest.objects.get(id=pk)
        lines = [
            'Reiseantrag',
            ' ',
            'Mitarbeiter: ' + travel_request_data.employee,
            'Reiseziel: ' + travel_request_data.destination,
            'Veranstaltung: ' + travel_request_data.event,
            'Reisebeginn: ' + str(travel_request_data.journey_start),
            'Reiseende: ' + str(travel_request_data.journey_end),
            'Dienstbeginn: ' + str(travel_request_data.event_start),
            'Dienstende: ' + str(travel_request_data.event_end),
            'Transportmittel: ' + str(travel_request_data.transport),
            'Kostenstelle: ' + str(travel_request_data.cost_center)
        ]
    else:
        travel_invoice_data = TravelInvoice.objects.get(id=pk)
        lines = [
            'Reisekostenabrechnung',
            ' ',
            'Mitarbeiter: ' + travel_invoice_data.employee,
            'Reiseziel: ' + travel_invoice_data.destination,
            'Veranstaltung: ' + travel_invoice_data.event,
            'Reisebeginn: ' + str(travel_invoice_data.journey_start),
            'Reiseende: ' + str(travel_invoice_data.journey_end),
            'Dienstbeginn: ' + str(travel_invoice_data.event_start),
            'Dienstende: ' + str(travel_invoice_data.event_end),
            'Übernachtungskosten: ' + str(travel_invoice_data.hotel_costs),
            'Fahrtkosten: ' + str(travel_invoice_data.transport_costs),
            'Nebenkosten: ' + str(travel_invoice_data.other_costs),
        ]
    for line in lines:
        text.textLine(line)
    page.drawText(text)
    page.showPage()
    page.save()
    file_buffer.seek(0)
    return FileResponse(file_buffer, as_attachment=True, filename='Travel-PDF.pdf')


def logout_view(request):
    logout(request)
