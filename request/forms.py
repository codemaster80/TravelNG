from django.forms import *
from request.models import *


class RequestForm(ModelForm):
    class Meta:
        model = TravelRequest
        fields = '__all__'
