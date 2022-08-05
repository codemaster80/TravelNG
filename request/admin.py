from django.contrib import admin
from request.models import *

# Register your models here.

admin.site.register(CostCenter)
admin.site.register(Employee)
admin.site.register(Transport)
admin.site.register(TravelRequest)
admin.site.register(TravelInvoice)