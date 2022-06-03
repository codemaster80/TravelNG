from django.db import models


# Create your models here.
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


class TravelRequest(models.Model):
    destination = models.CharField(max_length=50)
    event = models.CharField(max_length=50)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.destination} {self.event}'
