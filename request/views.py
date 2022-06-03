from django.http import HttpResponse
from django.shortcuts import render
from request.models import *


# Create your views here.
def start_request(request):
    return render(request, 'request/base.html', {'page_title':'Reiseantrag'})
