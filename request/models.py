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


class TravelRequest(models.Model):
    STATUS_CHOICES = [('Wartet', 'Wartet'),
                      ('Genehmigt', 'Genehmigt'),
                      ]

    destination = models.CharField(max_length=50, blank=False)
    event = models.CharField(max_length=50, blank=False)
    journey_start = models.DateTimeField(default='01.01.2022 08:00', blank=False)
    journey_end = models.DateTimeField(default='01.01.2022 08:00', blank=False)
    event_start = models.DateTimeField(default='01.01.2022 08:00', blank=False)
    event_end = models.DateTimeField(default='01.01.2022 08:00', blank=False)
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True, blank=False)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=False)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True, blank=False)
    status = models.CharField(default='Wartet', max_length=30, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.destination} {self.event}'


class TravelInvoice(models.Model):
    STATUS_CHOICES = [('Wartet', 'Wartet'),
                      ('Genehmigt', 'Genehmigt'),
                      ]

    hotel_costs = models.IntegerField(blank=False)
    transport_costs = models.IntegerField(blank=False)
    other_costs = models.IntegerField(blank=False)
    upload = models.FileField(upload_to='uploads/%Y%m%d-%H%M%S', null=True)
    status = models.CharField(default='Wartet', max_length=30, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.hotel_costs} {self.transport_costs} {self.other_costs}'
