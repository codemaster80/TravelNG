from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)


class CostCenter(models.Model):
    department = models.CharField(max_length=50)
    cost_center_number = models.IntegerField()


class TravelRequest(models.Model):
    destination = models.CharField(max_length=50)
    event = models.CharField(max_length=50)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
