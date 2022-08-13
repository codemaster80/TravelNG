"""TravelNG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import request.views
from TravelNG import settings
from request.views import home, logout_view, delete_travel_request, travel_auth

urlpatterns = [
    path('', home, name="home"),
    path(r'Request/Add/$', request.views.travel_request_details, name="addTravelRequest"),
    path(r'Request/Edit/(?P<pk>[0-9]+)/?$', request.views.travel_request_details, name="editTravelRequest"),
    path('deleteRequest/<int:item_id>', delete_travel_request, name="deleteTravelRequest"),
    path(r'Invoice/Add/$', request.views.travel_invoice_details, name="addTravelInvoice"),
    path(r'Invoice/Edit/(?P<pk>[0-9]+)/?$', request.views.travel_invoice_details, name="editTravelInvoice"),
    path(r'Invoice/Delete/<int:item_id>', request.views.delete_travel_invoice, name="deleteTravelInvoice"),
    path('travelAuth/', travel_auth, name="travelAuth"),
    path('travelInvoice/', request.views.travel_invoice, name="travelInvoice"),
    path('logout/', logout_view, {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
