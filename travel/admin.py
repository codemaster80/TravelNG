from travel.models import *
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(CostCenter)
admin.site.register(Transport)
admin.site.register(TravelRequest)
admin.site.register(TravelInvoice)
