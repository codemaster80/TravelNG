from django.db import models

# Create your models here.
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.surname} {self.name}'


class CostCenter(models.Model):
    department = models.CharField(max_length=50)
    cost_center_number = models.IntegerField()

    def __str__(self):
        return f'{self.department}'


class Transport(models.Model):
    vehicle = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.vehicle}'


class TravelRequestStatus(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.status}'


class TravelRequest(models.Model):
    destination = models.CharField(max_length=50, blank=False)
    event = models.CharField(max_length=50, blank=False)
    journey_start = models.DateTimeField(default=timezone.now, blank=False)
    journey_end = models.DateTimeField(default=timezone.now, blank=False)
    event_start = models.DateTimeField(default=timezone.now, blank=False)
    event_end = models.DateTimeField(default=timezone.now, blank=False)
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True, blank=False)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=False)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True, blank=False)
    status = models.ForeignKey(TravelRequestStatus, default='wartet', on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return f'{self.destination} {self.event}'


class TravelInvoiceStatus(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.status}'


class TravelInvoice(models.Model):
    hotel_costs = models.IntegerField(blank=False)
    transport_costs = models.IntegerField(blank=False)
    other_costs = models.IntegerField(blank=False)
    status = models.ForeignKey(TravelInvoiceStatus, default='wartet', on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return f'{self.hotel_costs} {self.transport_costs} {self.other_costs}'
