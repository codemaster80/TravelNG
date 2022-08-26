from django.contrib import admin
from travel.models import *

# Register your models here.

admin.site.register(CostCenter)
admin.site.register(Transport)
admin.site.register(TravelRequest)
admin.site.register(TravelInvoice)
