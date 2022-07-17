from django.http import HttpResponse
from django.shortcuts import render, redirect
from request.models import *


# Create your views here.
def home(request):
    return render(request, 'request/base.html', {'page_title': 'Start'})


def new_request(request):
    return redirect("http://www.google.de")


def new_invoice(request):
    return redirect("http://www.google.de")
