import uuid
from fileinput import filename

from django.db import models

# Create your models here.
from django.db.models.fields.files import FieldFile
from django.utils import timezone


class CostCenter(models.Model):
    department = models.CharField(max_length=50)
    cost_center_number = models.IntegerField()

    def __str__(self):
        return f'{self.department}'


class Transport(models.Model):
    vehicle = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.vehicle}'


class TravelRequest(models.Model):
    STATUS_CHOICES = [('In Bearbeitung', 'In Bearbeitung'),
                      ('Genehmigt', 'Genehmigt'),
                      ]

    username = models.CharField(max_length=50, null=True, blank=False)
    employee = models.CharField(max_length=50, null=True, blank=False)
    destination = models.CharField(max_length=50, blank=False)
    event = models.CharField(max_length=50, blank=False)
    journey_start = models.DateTimeField(default='01.01.2022 08:00', blank=False)
    journey_end = models.DateTimeField(default='01.01.2022 08:00', blank=False)
    event_start = models.DateTimeField(default='01.01.2022 08:00', blank=False)
    event_end = models.DateTimeField(default='01.01.2022 08:00', blank=False)
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True, blank=False)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True, blank=False)
    status = models.CharField(default='In Bearbeitung', max_length=30, choices=STATUS_CHOICES)

    class Meta:
        permissions = [
            (
                'is_supervisor', 'can access auth page'
            )
        ]

    def __str__(self):
        return f'{self.destination} {self.event}'


class TravelInvoice(models.Model):
    STATUS_CHOICES = [('In Bearbeitung', 'In Bearbeitung'),
                      ('Auszahlung angewiesen', 'Auszahlung angewiesen'),
                      ]

    username = models.CharField(max_length=50, null=True, blank=False)
    employee = models.CharField(max_length=50, null=True, blank=False)
    travel_request = models.OneToOneField(TravelRequest, on_delete=models.SET_NULL, null=True, blank=False)
    destination = models.CharField(max_length=30, null=True, blank=True)
    event = models.CharField(max_length=30, null=True, blank=True)
    journey_start = models.DateTimeField(null=True, blank=True)
    journey_end = models.DateTimeField(null=True, blank=True)
    event_start = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)
    hotel_costs = models.IntegerField(blank=False)
    transport_costs = models.IntegerField(blank=False)
    other_costs = models.IntegerField(blank=False)
    upload = models.FileField(upload_to='invoiceData/' + str(uuid.uuid4()), null=True, blank=True)
    tr_status = models.CharField(default='In Bearbeitung', max_length=30, null=True, blank=True)
    ti_status = models.CharField(default='In Bearbeitung', max_length=30, choices=STATUS_CHOICES)

    class Meta:
        permissions = [
            (
                'is_clerk', 'can access invoice page'
            )
        ]

    def __str__(self):
        return f'{self.hotel_costs} {self.transport_costs} {self.other_costs}'
